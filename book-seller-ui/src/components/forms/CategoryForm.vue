<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const isEditing = route.params.id ? ref(true) : ref(false)
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
            v-model="category"
          />
          <label for="floatingInput">Section name</label>
        </div>

        <div class="d-flex gap-1 w-100">
          <button type="button" v-if="!isEditing" class="btn btn-success">Add New</button>
          <button type="button" v-else class="btn btn-info">Update</button>
          <RouterLink to="/categories">
            <button type="button" class="btn btn-secondary me-2">Cancel</button>
          </RouterLink>
        </div>
      </form>
    </div>
  </div>
</template>
<style scoped></style>
