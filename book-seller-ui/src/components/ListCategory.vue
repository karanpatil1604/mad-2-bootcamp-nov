<script setup>
import { RouterLink } from 'vue-router'
import { computed, onBeforeMount, ref } from 'vue'
import ApiService from '@/services/ApiService'
const categories = ref([])

const fetchCategories = async () => {
  const res = await ApiService.get('/categories')
  categories.value = res
  console.log(res)
}

onBeforeMount(fetchCategories)

const activeCategories = computed(() => {
  return categories.value.filter((cat) => cat.isActive == true || cat.isActive == 0)
})
</script>
<template>
  <div class="d-flex justify-content-between align-items-center px-4 mt-2">
    <h1>List of All Categories</h1>
    <RouterLink to="/categories/new" class="text-decoration-none">
      <button class="btn btn-primary">+Add New</button>
    </RouterLink>
  </div>
  <div class="row">
    <div class="col px-5 mx-5 mt-4">
      <ul class="list-group">
        <li class="list-group-item" v-for="cat in activeCategories" :key="cat.id">
          {{ cat.name }} | {{ cat.isActive }}
        </li>
      </ul>
    </div>
  </div>
</template>
