<script setup>
import { RouterLink } from 'vue-router'
import { ref } from 'vue'
import NavItem from './NavItem.vue'

import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()
const q = ref('')

const emit = defineEmits(['inputValue', 'atSearch'])

let l = [1, 2, 4]
console.log(...l)

const handleSearch = () => {
  const query = { ...route.query, q: q.value }
  router.push({ query })
}
</script>

<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <RouterLink class="text-decoration-none" to="/">
        <div class="navbar-brand">Bookstore</div>
      </RouterLink>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <NavItem route="/">Home </NavItem>
          <NavItem route="/about">About</NavItem>

          <NavItem route="/categories">Categories</NavItem>

          <li class="nav-item dropdown">
            <a
              class="nav-link dropdown-toggle"
              href="#"
              role="button"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              Acccount
            </a>
            <ul class="dropdown-menu">
              <RouterLink class="text-decoration-none" to="/login">
                <li class="dropdown-item">Login</li>
              </RouterLink>
              <RouterLink class="text-decoration-none" to="/register">
                <li class="dropdown-item">Register</li>
              </RouterLink>
              <li><hr class="dropdown-divider" /></li>
              <li><a class="dropdown-item" href="#">Logout</a></li>
            </ul>
          </li>
        </ul>
        <form class="d-flex" role="search">
          <input
            class="form-control me-2"
            type="search"
            v-model="q"
            placeholder="Search"
            aria-label="Search"
          />
          <button class="btn btn-outline-success" @click="handleSearch" type="button">
            Search
          </button>
        </form>
      </div>
    </div>
  </nav>
</template>
