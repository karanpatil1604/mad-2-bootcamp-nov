from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.exc import UnmappedInstanceError
from flask_cors import CORS
from flask_caching import Cache

from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError
import jwt

from models import db, User, Category


import workers
import tasks


app = Flask(__name__)
api = Api(app)

CORS(
    app, resources={r"/*": {"origins": ["http://example.com", "http://localhost:5173"]}}
)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SECRET_KEY"] = "my_secret_key"
app.config["CELERY_BROKER_URL"] = "redis://localhost:6379/1"
app.config["CELERY_RESULT_BACKEND"] = "redis://localhost:6379/2"
app.config["CACHE_TYPE"] = "RedisCache"
app.config["CACHE_REDIS_DB"] = "0"
app.config["CACHE_REDIS_URL"] = "redis://localhost:6379/0"
# app.config["CACHE_REDIS_HOST"] = "redis://localhost"
# app.config["CACHE_REDIS_PORT"] = "6379"
# app.config["CACHE_DEFAULT_TIMEOUT"] = 300

db.init_app(app)

celery = workers.celery
cache = Cache(app)

celery.conf.update(
    broker_url=app.config["CELERY_BROKER_URL"],
    result_backend=app.config["CELERY_RESULT_BACKEND"],
)
celery.conf.update(
    result_expires=3600,
    task_soft_time_limit=300,
    task_time_limit=600,
)

celery.Task = workers.ContextTask
app.app_context().push()


class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}

    def post(self):
        return {"post": "request"}

    def put(self):
        return "put request handled"

    def delete(self):
        return "delete request handled"


from flask_restful import reqparse, fields, marshal, marshal_with

res_fields = {"id": fields.Integer, "name": fields.String, "isActive": fields.Boolean}


class CategoryList(Resource):
    @cache.cached(timeout=60)
    def get(self):
        page = request.args.get("page", 1)
        per_page = request.args.get("per_page", 2)
        if page:
            categories = Category.query.paginate(page=int(page), per_page=int(per_page))
            items = [
                {"id": cat.id, "name": cat.name, "isActive": cat.isActive}
                for cat in categories.items
            ]
            return {
                "items": items,
                "page": categories.page,
                "per_page": categories.per_page,
                "total": categories.total,
                "pages": categories.pages,
            }
        else:
            categories = Category.query.all()
            res = [
                {"id": cat.id, "name": cat.name, "isActive": cat.isActive}
                for cat in categories
            ]

            # for cat in categories:
            #     next_cat = {"id": cat.id, "name": cat.name, "isActive": cat.isActive}
            #     res.append(next_cat)
            return res

    def post(self):
        data = request.get_json()
        print(data)
        print(type(data))
        cat_name = data.get("name")
        new_category = Category(name=cat_name, isActive=1)
        db.session.add(new_category)
        db.session.commit()
        return {
            "message": "Category created successfully",
            "id": new_category.id,
            "name": new_category.name,
            "isActive": new_category.isActive,
        }


class CategoryDetail(Resource):
    def get(self, id):
        category = Category.query.get(id)
        if not category:
            return {"message": "Category does not exist"}, 404
        return {
            "message": "Category details",
            "id": category.id,
            "name": category.name,
            "isActive": category.isActive,
        }, 200

    def put(self, id):
        category = Category.query.get(id)
        data = request.get_json()
        new_cat_name = data.get("name")
        new_status = data.get("isActive")
        category.name = new_cat_name
        category.isActive = new_status
        db.session.commit()
        return (
            {
                "message": "Category details are updated!",
                "id": category.id,
                "name": category.name,
                "isActive": category.isActive,
            },
            200,
        )

    def delete(self, id):
        try:
            category = Category.query.get(id)
            if not category:
                raise Exception(404)
            db.session.delete(category)
            db.session.commit()
        except UnmappedInstanceError as e:
            return {
                "message": "Category with the id does not exist",
                "error": str(e),
            }, 500
        return {
            "message": "Category deleted successfully!",
        }, 200


api.add_resource(HelloWorld, "/")
api.add_resource(CategoryList, "/categories")
api.add_resource(CategoryDetail, "/categories/<id>")


@app.route("/search")
def search():
    query = request.args.get("q", "")
    query = f"%{query}%"
    if query:
        categories = Category.query.filter(Category.name.ilike(query)).all()

    return marshal(categories, res_fields)


@app.post("/login")
def login():
    email = request.json.get("email")
    password = request.json.get("password")
    user = User.query.filter_by(email=email).first()
    if user:
        if check_password_hash(user.password, password):
            token = jwt.encode(
                {
                    "user_id": user.id,
                    "email": user.email,
                    "role": user.role,
                },
                app.config["SECRET_KEY"],
            )
            return jsonify({"token": token}), 200
        else:
            # WRONG PASSWORD
            return jsonify({"msg": "Incorrect Username or Email!"}), 400

    return jsonify({"msg": "Incorrect Username or Email!"}), 404


@app.post("/register")
def register():
    credentials = request.get_json()
    try:
        new_user = User(
            first_name=credentials.get("fname", ""),
            last_name=credentials["lname"],
            email=credentials["email"],
            role=credentials["role"],
            password=generate_password_hash(credentials["password"]),
        )
        db.session.add(new_user)
        db.session.commit()
        # event generated (A task defined by the developer)
        # send_mail_task()
    except IntegrityError:
        return (
            jsonify(
                {
                    "msg": "Integrity Error",
                    "details": {
                        "field": "email",
                        "error": "User with this email or username already exist",
                    },
                }
            ),
            409,
        )
    return {"msg": "CREATED NEW USER", "new_user_id": new_user.id}


@app.route("/hello/<name>")
def hello_job(name):
    if not name:
        name = "Karan"
    job = tasks.just_say_hello.delay(name)

    return str(job), 200


# BASE_URL = http://localhot:5000

# Actions

# 1. Listing -> GET request which return the List of the requested Entity
# /categories

# 2. Create
# /categories -> POST request sent along with the request body which carries data for the new object

# ========================================

# 3. Retrieve
# /categories/<id> -> GET request is send to fetch/retrieve a single object of the Entity

# 4. Update
# /categories/<id> -> PUT request is sent along with 'NEW DATA' and the existing Entity will be updated

# 5. Delete
# /categories/<id> -> DELETE request is sent and the Entity is deleted


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
