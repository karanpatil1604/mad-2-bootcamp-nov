<script setup>
import { ref } from 'vue'
import BookCard from '@/components/cards/BookCard.vue'

const dummy_book = ref({
  id: 1,
  title: 'Book title 1',
  num_of_pages: 256,
})

const books = ref([
  {
    id: 1,
    title: 'Book title 1',
    num_of_pages: 256,
  },
  {
    id: 2,
    title: 'Book title 2',
    num_of_pages: 256,
  },
  {
    id: 3,
    title: 'Book title 3',
    num_of_pages: 256,
  },
  {
    id: 4,
    title: 'Book title 1',
    num_of_pages: 256,
  },
  {
    id: 5,
    title: 'Book title 2',
    num_of_pages: 256,
  },
  {
    id: 6,
    title: 'Book title 3',
    num_of_pages: 256,
  },
])
</script>

<template>
  <main>
    <div class="row g-3 g-md-2 mx-2 mx-md-4">
      <div class="col-md-3 col-6" v-for="book in books" :key="book.id">
        <BookCard :book="book" />
      </div>
    </div>

    <!-- <div class="row g-3">
      <div class="col-12 bg-primary">
        <div class="row">
          <div class="col-3 offset-3 border border-secondary">2</div>
          <div class="col-3 border border-danger">3</div>
          <div class="col-3 border border-primary">4</div>
        </div>
      </div>
      <div class="col bg-secondary">two</div>
      <div class="col bg-warning">three</div>
    </div>

    <div class="d-flex border border-danger justify-content-center gap-3">
      <div class="p-2 border border-warning">Flex item 1</div>
      <div class="p-2 border border-warning">Flex item 2</div>
      <div class="p-2 border border-warning">Flex item 3</div>
    </div> -->
  </main>
</template>
