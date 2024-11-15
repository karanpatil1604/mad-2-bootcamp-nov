<script setup>
import { ref } from 'vue'

const credintials = ref({
  email: '',
  password: '',
})
// validity check

const handleLogin = () => {
  // 1. collect the data from form
  console.log('Making an API call to login endpoint')
  // 2. Make an api call to send data to the backend
  console.log('This is ref object', credintials.value)
  // 3. Display the response to the user
  console.log('Response recieved succesfully')
}
</script>
<template>
  <div class="container-fluid d-flex flex-column justify-content-around pb-2">
    <div class="shadow rounded-1 p-4 mt-4 col-md-4 offset-md-4">
      <div class="mt-2">
        <div class="text-center fw-semibold fs-2">Login</div>
      </div>
      <hr />
      <form class="fs-6">
        <div class="form-floating mb-3">
          <input
            type="email"
            class="form-control"
            id="floatingInput"
            placeholder="name@example.com"
            v-model="credintials.email"
          />
          <label for="floatingInput">Email address</label>
        </div>
        <div class="form-floating">
          <input
            type="password"
            class="form-control"
            id="floatingPassword"
            placeholder="Password"
            v-model="credintials.password"
          />
          <label for="floatingPassword">Password</label>
        </div>
        <div class="mb-3 form-text">
          Don't have an account?
          <router-link to="/register">Register</router-link>
        </div>

        <div class="text-start d-flex flex-column gap-1 w-100">
          <button type="button" @click="handleLogin" class="btn btn-primary">Log In</button>
        </div>
      </form>
    </div>
  </div>
</template>
<style scoped></style>
