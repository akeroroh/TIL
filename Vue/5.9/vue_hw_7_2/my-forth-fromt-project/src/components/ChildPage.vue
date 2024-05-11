<template>
    <div class="childbox">
        <h3>자식 페이지</h3>
        <p>{{children.name}}</p>
    </div>
</template>

<script setup>
defineProps({
    children: Object,
})
</script>

<style scoped>
.childbox{
    border: 1px solid lightgray;
    background-color: white;
    margin: 10px
}
</style>