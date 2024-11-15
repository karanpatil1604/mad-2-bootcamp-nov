from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.exc import UnmappedInstanceError
from flask_cors import CORS

db = SQLAlchemy()


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    isActive = db.Column(db.Integer, default=0)


app = Flask(__name__)
api = Api(app)

CORS(
    app, resources={r"/*": {"origins": ["http://example.com", "http://localhost:5173"]}}
)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db.init_app(app)


class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}

    def post(self):
        return {"post": "request"}

    def put(self):
        return "put request handled"

    def delete(self):
        return "delete request handled"


class CategoryList(Resource):
    def get(self):
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
        new_category = Category(name=cat_name)
        db.session.add(new_category)
        db.session.commit()
        return {
            "message": "Recieved the data correctly",
            "id": new_category.id,
            "name": new_category.name,
            "isActive": new_category.isActive,
        }


class CategoryDetail(Resource):
    def get(self, id):
        category = Category.query.get(id)
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
