<script setup>
import { RouterView } from 'vue-router'
import Navbar from './components/navbar/Navbar.vue'
import AlertMessage from './components/popups/AlertMessage.vue'
import { provide, ref } from 'vue'

const searchQuery = ref('')
const setQuery = (inputText) => {
  searchQuery.value = inputText
  console.log('This is my query', searchQuery.value)
}
provide('query', searchQuery.value)
</script>

<template>
  <header>
    <Navbar @atSearch="setQuery"></Navbar>
  </header>

  <RouterView />
  <AlertMessage />
</template>

<style scoped></style>
