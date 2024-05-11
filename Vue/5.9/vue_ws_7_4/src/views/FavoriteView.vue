<template>
<div>
    <h1>장바구니 페이지</h1>
</div>
<div class="cardcontainer">
    <div class="card" v-for="item in store.favoriteitem" :item="item" :key="item.id">
        <h3>{{ item.name }}</h3>
        <img :src= "item.imagePath" alt="">
        <p>&#8361 {{ item.price }}</p>
        <p @click="store.updatefavorite(item.name)">{{ item.isFavorite? '&#9829': '&#9825' }}</p>
    </div>
</div>

</template>

<script setup>
import { useProductStore } from '@/stores/products';
const store = useProductStore()
</script>

<style scoped>
.cardcontainer{
    display: flex;
    flex-wrap: wrap;
}
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