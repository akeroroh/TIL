
<template>
  <header>
    <nav>
      <router-link :to="{ name: 'home' }">Home</router-link>
      <span> | </span>
      <router-link :to="{ name: 'about' }">About</router-link>
    </nav>
  </header>
  <router-view />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
</style>
