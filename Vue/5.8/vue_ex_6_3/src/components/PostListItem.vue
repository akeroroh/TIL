<template>
<li>
    <p>제목: {{ post.name }}</p>
</li>
</template>

<script setup>
defineProps({
    post: Object,
})
</script>

<style scoped>

</style>