<script setup>
import { RouterView } from 'vue-router'
import Navbar from './components/navbar/Navbar.vue'
import AlertMessage from './components/popups/AlertMessage.vue'
</script>

<template>
  <header>
    <Navbar></Navbar>
  </header>

  <RouterView />
  <AlertMessage />
</template>

<style scoped></style>
