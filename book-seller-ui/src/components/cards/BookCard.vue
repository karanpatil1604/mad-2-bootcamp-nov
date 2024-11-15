<script setup>
const props = defineProps({
  book: Object,
})
</script>
<template>
  <div class="card shadow shadow-sm">
    <div
      class="card-header d-flex g-1 align-items-center justify-content-between text-black font-bold"
    >
      <span class="title">{{ book.title }}</span>
      <!-- <div v-if="userRole === 'admin'" class="d-flex gap-2 justify-content-between">
          <RouterLink
            :to="{
              name: 'bookEdit',
              params: { id: book.id },
            }"
          >
            <button class="btn btn-outline-info" type="button">
              <i class="bi bi-pencil-square"></i>
            </button>
          </RouterLink>
          <button class="btn btn-outline-danger" @click.prevent="deleteBook">
            <i class="bi bi-trash3"></i>
          </button>
        </div> -->
    </div>
    <img src="@/assets/placeholder.png" />
    <div class="card-body py-1 px-2">
      <div class="d-flex justify-content-around align-items-center my-2">
        <span class="">{{ book.num_of_pages }} Pages</span>
        <span class="">Rent: $ {{ 19.99 + book.id }}</span>
      </div>
      <button type="submit" class="btn btn-warning rounded w-100 my-2">Rent</button>
    </div>
  </div>
</template>

<style scoped>
.title {
  font: 1.3rem bold;
}

img {
  border-radius: 0;
  position: relative;

  aspect-ratio: 0.85;
}
</style>
