<template>
    <div>
        <h1>데이터 수정 페이지</h1>
        <p>이름: {{ store.correctBalance.name }}</p>
        <p>잔고: {{ store.correctBalance.balance }}</p>
        <button @click="store.plusBalance()">+</button>
    </div>
</template>

<script setup>
import {useBalanceStore} from '@/stores/balance'
const store = useBalanceStore()
</script>

<style scoped>

</style>