<template>
{{ product.name }} - {{ product.price }}원 <button>장바구니에 추가</button>
</template>

<script setup>
defineProps({
    product: Array
})
</script>

<style lang="scss" scoped>

</style>