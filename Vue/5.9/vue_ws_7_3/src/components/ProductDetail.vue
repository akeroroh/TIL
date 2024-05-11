<template>
<div class="card">
    <h3>{{ product.name }}</h3>
    <img :src= "product.imagePath" alt="">
    <p>&#8361 {{ product.price }}</p>
    <p @click="store.updatefavorite(product.name)">{{ product.isFavorite? '&#9829': '&#9825' }}</p>
</div>
</template>

<script setup>
import {useProductStore} from '@/stores/products'
defineProps({
    product: Object,
})
const store = useProductStore()
</script>

<style scoped>
*{
    box-sizing: border-box
}
.card{
    width: 350px;
    height: 400px;
    border: 2px solid lightgray;
    text-align: center;
    padding: 20px 5px;
    margin: 10px
}
img{
    width: 300px;
    height: 180px;
    margin: 0
}
</style>