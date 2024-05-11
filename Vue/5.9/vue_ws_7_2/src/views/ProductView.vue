<template>
    <div>
        <h1>상품 목록 페이지</h1>
        <ProductDetail 
        v-for="product in store.productList"
        :key="product.id"
        :product="product"
        />
    </div>
</template>

<script setup>
import ProductDetail from '@/components/ProductDetail.vue'
import {useProductStore} from '@/stores/products'

const store = useProductStore()

</script>

<style scoped>

</style>