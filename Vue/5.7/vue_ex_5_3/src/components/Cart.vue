<template>
<h2>장바구니</h2>
<ul>
    <li v-for="cartitem in cartitems" :key="cartitem.id">
        {{cartitem.name}} - {{cartitem.price}}원 
        <button @click="deleteCartItem(cartitem)">삭제</button>
    </li>
</ul>
</template>

<script setup>
defineProps({
    cartitems: Array,
})

const emit = defineEmits(['deleteCartItem'])
const deleteCartItem = function(cartitem) {
    emit('deleteCartItem', cartitem)
}
</script>

<style lang="scss" scoped>

</style>