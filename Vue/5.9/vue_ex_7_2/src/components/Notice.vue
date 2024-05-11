<template>
<p>남은 제품 개수 : {{ store.productCount }}</p>
</template>

<script setup>
import {useProductStore} from '@/stores/product'
const store = useProductStore()
</script>

<style scoped>

</style>