<script setup>
import { onBeforeMount, onMounted, ref } from 'vue'
import AlertService from '@/services/AlertService.js'
import ApiService from '@/services/ApiService'
const categories = ref([])

onMounted(() => {
  AlertService.showAlert('We are on category list page', 'success', 5000)
})
</script>
<template>
  <RouterView></RouterView>
</template>
<style scoped></style>
