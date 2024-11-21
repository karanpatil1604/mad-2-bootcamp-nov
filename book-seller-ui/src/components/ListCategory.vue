<script setup>
import { RouterLink, useRoute } from 'vue-router'
import { computed, onBeforeMount, ref, watch } from 'vue'
import ApiService from '@/services/ApiService'
import AlertService from '@/services/AlertService'

const route = useRoute()
const categories = ref([])

const fetchCategories = async () => {
  const res = await ApiService.get('/categories')
  categories.value = res.items
}

onBeforeMount(fetchCategories)

const activeCategories = computed(() => {
  return categories.value.filter((cat) => cat.isActive == true)
})

const handleDelete = async (cat_id) => {
  let confirmation = confirm('Do you really want to delete the category?')
  if (confirmation) {
    const res = await ApiService.delete(`/categories/${cat_id}`)
    AlertService.showAlert('Category deleted successfully!', 'info')
    fetchCategories()
  }
}

watch(
  () => route.query.q,
  async (newQuery) => {
    // /search?q=cat
    const res = await ApiService.get(`/search?q=${newQuery}`)
    console.log(res)

    categories.value = res
    console.log('These are my query q in child componetn:', newQuery)
  },
  { immediate: true },
)
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
        <li
          class="list-group-item d-flex justify-content-between px-3"
          v-for="cat in activeCategories"
          :key="cat.id"
        >
          <div>{{ cat.name }} | {{ cat.isActive }}</div>
          <div class="d-flex gap-3">
            <RouterLink :to="{ name: 'edit-category', params: { id: cat.id } }">
              <div class="btn btn-warning">Edit</div>
            </RouterLink>

            <div class="btn btn-danger" @click.prevent="handleDelete(cat.id)">Delete</div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>
