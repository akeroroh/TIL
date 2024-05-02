<template>
  <header class="sticky-top bg-success-subtle p-3">
    <div class='text-center'>
      <h1 class="fw-bold">My Gallery</h1>
    </div>
  </header>

  <main class="container py-3">
    <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3 ">
      <div class="col" v-for="index in numberOfItems" :key="index">
        <div class="card">
          <img src="@\assets\sample.png" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
            <a href="#" class="btn btn-primary">Go somewhere</a>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script setup>
  import { ref } from 'vue';

  const numberOfItems = ref(4);
</script>

<style scoped>
</style>
