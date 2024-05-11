<template>
    <div>
        <p>이름: {{ balance.name }}</p>
        <p>잔고: {{ balance.balance }}</p>
        <button @click="updateroute(balance)">updateBalance</button>
        <hr>
    </div>
</template>

<script setup>
import {useRouter, useRoute} from 'vue-router'
defineProps({
    balance: Object
})
const route = useRoute()
const router =useRouter()

const updateroute = function(balance) {
    router.push({name: 'update', params: {'name': balance.name}})
}
</script>

<style scoped>
button{
    width: 110px;
    background-color: #007BFF;
    border: 1px solid #007BFF;
    color: white;
    padding: 5px;
    border-radius: 5px;
}
</style>