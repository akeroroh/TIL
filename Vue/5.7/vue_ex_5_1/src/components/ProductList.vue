<template>
<li v-for="product in products" :key="product.id">
    {{ product.name }} - {{ product.price }}
</li>
</template>

<script setup>
defineProps({
    products: Array
})
</script>

<style scoped>

</style>