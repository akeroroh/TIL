<script setup>
import MainPage from '@/components/MainPage.vue'
</script>

<template>
  <MainPage/>
  <RouterLink :to="{name: 'some'}">Some</RouterLink>
  <span> | </span>
  <RouterLink :to="{name: 'other'}">Other</RouterLink>
  <router-view />
</template>

<style scoped>
</style>
