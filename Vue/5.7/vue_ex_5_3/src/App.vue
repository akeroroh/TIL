<template>
  <div>
    <h1>쇼핑 애플리케이션</h1>
    <ProductList :products="products" @add-to-cart="addToCart"/>
    <p>총 가격: {{ totalCartPrice }}원</p>
    <Cart :cartitems="cartitems" @delete-cart-item="deleteCartItem"/>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import ProductList from '@/components/ProductList.vue'
import Cart from '@/components/Cart.vue'

let id = 0

const products = ref([
  { id: id++, name: '사과', price: 1000 },
  { id: id++, name: '바나나', price: 1500 },
  { id: id++, name: '딸기', price: 2000 },
  { id: id++, name: '포도', price: 3000 },
  { id: id++, name: '복숭아', price: 2000 },
  { id: id++, name: '수박', price: 5000 }
])

const cartitems = ref([])


const totalCartPrice = computed(() => {
  return cartitems.value.reduce((total, item) => total + item.price, 0);
});

const addToCart = function(product) {
  cartitems.value.push(product)
}

const deleteCartItem = function(cartItem) {
  const index = cartitems.value.indexOf(cartItem);
  if (index !== -1) {
    cartitems.value.splice(index, 1);
  }
};</script>
