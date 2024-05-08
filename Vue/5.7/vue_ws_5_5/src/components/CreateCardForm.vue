<template>
<form @submit.prevent="createCardFunc">
    <label for="name">이름 </label>
    <input type="text" id="name" v-model="name">
    <label for="title"> 직함 </label>
    <input type="text" id="title" v-model="title">
    <button type="submit">명함 추가</button>
</form>
</template>

<script setup>
import { ref } from 'vue'

const emit = defineEmits(['createCard'])
const name = ref('')
const title = ref('')

const createCardFunc = function() {
    const cardInfo = {
        'name': name.value,
        'title': title.value,
    }
    emit('createCard', cardInfo)
    name.value = ''
    title.value = ''
}
</script>

<style scoped>
input{
    border: 1px solid cornflowerblue;
    border-radius: 5px;
    height: 35px;
    width: 275px;
}
button{
    border: 1px solid cornflowerblue;
    border-radius: 5px;
    height: 39px;
    width: 100px;  
    margin: 10px;
    background-color: white;
    color: cornflowerblue
}
</style>