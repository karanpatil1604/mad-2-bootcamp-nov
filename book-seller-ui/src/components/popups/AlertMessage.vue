<script setup>
import { computed } from 'vue'
import AlertService from '@/services/AlertService.js'

const messages = computed(() => AlertService.state.messages)
</script>

<template>
  <div v-if="messages.length" class="alert-container">
    <div
      v-for="(msg, index) in messages"
      :key="index"
      class="alert"
      :class="`alert-${msg.type}`"
      role="alert"
    >
      {{ msg.message }}
    </div>
  </div>
</template>

<style scoped>
.alert-container {
  position: fixed;
  bottom: 20px;
  right: 20px;
  z-index: 1050;
}

.alert {
  margin-bottom: 10px;
  transition: opacity 0.5s;
}

.alert-info {
  background-color: #d1ecf1;
  color: #0c5460;
}

.alert-success {
  background-color: #d4edda;
  color: #155724;
}

.alert-warning {
  background-color: #fff3cd;
  color: #856404;
}

.alert-danger {
  background-color: #f8d7da;
  color: #721c24;
}
</style>
