<template>
<nav class="navbar">
  <RouterLink class="navlink" :to="{name: 'home'}">Home</RouterLink>
  <span class="navspace"></span>
  <RouterLink class="navlink" :to="{name: 'products'}">products</RouterLink>
  <span class="navspace"></span>
  <RouterLink class="navlink" :to="{name: 'favorite'}">Favorite</RouterLink>
  <div v-if="store.countFavorite !== 0" class="countfavorite">{{ store.countFavorite }}</div>
</nav>
<RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import {useProductStore} from '@/stores/products'
const store = useProductStore()
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
.countfavorite{
  width: 20px;
  height: 20px;
  text-align: center;
  background-color: red;
  color: white;
  border: 1px solid red;
  border-radius: 50%;
  margin: 3px;
  display: flex;
  justify-content: center;
  align-items: center;
}

</style>