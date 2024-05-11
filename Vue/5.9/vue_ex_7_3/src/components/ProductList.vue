<!-- ProductList.vue -->
<template>
  <div>
    <h2>Product List</h2>
    <ul>
      <ProductListItem 
        v-for="product in store.products" 
        :key="product.id" 
        :product="product" 
      />
    </ul>
  </div>
</template>

<!-- <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script> -->
<script setup>
import ProductListItem from '@/components/ProductListItem.vue'
import { useProductStore } from '@/stores/product'

const store = useProductStore()
</script>
