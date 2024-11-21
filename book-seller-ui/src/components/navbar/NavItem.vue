<script setup>
const props = defineProps({
  route: {
    type: String,
    default: '/',
  },
})
</script>
<template>
  <div>
    <li class="nav-item">
      <RouterLink class="text-decoration-none" :to="props.route">
        <div class="navbar-brand">
          <slot></slot>
        </div>
      </RouterLink>
    </li>
    <p>
      <slot name="para"></slot>
    </p>
  </div>
</template>
<style scoped></style>
