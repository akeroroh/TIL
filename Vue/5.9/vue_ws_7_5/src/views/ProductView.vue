<template>
    <div>
        <h1>상품 목록 페이지</h1>
        <div class="cardcontainer">
            <ProductDetail 
            v-for="product in store.productList"
            :key="product.id"
            :product="product"
            />

        </div>
    </div>
</template>

<script setup>
import ProductDetail from '@/components/ProductDetail.vue'
import {useProductStore} from '@/stores/products'

const store = useProductStore()

</script>

<style scoped>
.cardcontainer{
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}
</style>