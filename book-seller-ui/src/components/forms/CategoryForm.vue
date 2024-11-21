<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import ApiService from '@/services/ApiService.js'
import AlertService from '@/services/AlertService.js'

const route = useRoute()
const router = useRouter()

const category = ref({
  id: '',
  name: '',
  isActive: 0,
})

const idParam = route.params.id
const isEditing = route.params.id ? ref(true) : ref(false)

const fetchCategory = async () => {
  const res = await ApiService.get(`/categories/${idParam}`)
  console.log(res)
  if (res.status == 404) {
    AlertService.showAlert('Category not found!', 'danger')
  }
  category.value.id = res.id
  category.value.name = res.name
  category.value.isActive = res.isActive
}

if (idParam && isEditing) {
  onMounted(fetchCategory)
}

const handleSubmit = async () => {
  if (isEditing && idParam) {
    const res = await ApiService.put(`/categories/${idParam}`, category.value)
    console.log(res)
    AlertService.showAlert('Category updated successfully!', 'info')
    router.push('/categories')
  } else {
    const res = await ApiService.post(`/categories`, { name: category.value.name })
    console.log(res)
    AlertService.showAlert('Category created successfully!', 'success')
    router.push('/categories')
  }
}

console.log(route.params.id)
</script>
<template>
  <div class="row mt-md-4 p-0 m-0">
    <div class="offset-md-4 col-md-4">
      <div class="row">
        <h2 v-if="!isEditing">Add New Category</h2>
        <h2 v-if="isEditing">Edit Category</h2>
      </div>
      <form class="fs-6">
        <div class="form-floating mb-3">
          <input
            type="text"
            class="form-control"
            id="floatingInput"
            placeholder="sectionName"
            v-model="category.name"
          />
          <label for="floatingInput">Section name</label>
        </div>

        <div class="d-flex gap-1 w-100">
          <button type="button" @click="handleSubmit" v-if="!isEditing" class="btn btn-success">
            Add New
          </button>
          <button type="button" v-else class="btn btn-info" @click="handleSubmit">Update</button>
          <RouterLink to="/categories">
            <button type="button" class="btn btn-secondary me-2">Cancel</button>
          </RouterLink>
        </div>
      </form>
    </div>
  </div>
</template>
<style scoped></style>
