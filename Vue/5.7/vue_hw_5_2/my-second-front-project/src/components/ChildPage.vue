<template>
<div v-for="child in children">
    <h3>자식 페이지입니다.</h3>
    <p>이름 : {{ child.name }}</p>
    <p>나이 : {{ child.age }}</p>
</div>
</template>

<script setup>
const props = defineProps({
    children: Array
})
</script>

<style scoped>
div{
    border: 1px solid lightgray;
    margin: 5px;
    padding: 10px
}
</style>