<script setup>
const props = defineProps({
  route: {
    type: String,
    default: '/',
  },
})
</script>
<template>
  <li class="nav-item">
    <RouterLink :to="props.route">
      <div class="navbar-brand">
        <slot></slot>
      </div>
    </RouterLink>
  </li>
  <p>
    <slot name="para"></slot>
  </p>
</template>
<style scoped></style>
