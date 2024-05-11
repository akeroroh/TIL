<template>
  <nav class="navbar">
    <RouterLink class="navlink" :to="{name: 'home'}">Home</RouterLink>
    <span class="navspace"></span>
    <RouterLink class="navlink" :to="{name: 'products'}">products</RouterLink>
    <span class="navspace"></span>
    <RouterLink class="navlink" :to="{name: 'favorite'}">Favorite</RouterLink>
  </nav>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
*{
box-sizing: border-box;
}
.navbar{
  background-color: #333333;
  width: 100%;
  display: flex;
  justify-content: center;
  padding: 10px
}
.navlink{
  color: white;
  text-decoration: none;
}
.navspace{
  width: 20px
}
</style>