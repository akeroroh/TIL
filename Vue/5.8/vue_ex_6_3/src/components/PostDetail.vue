<template>
<div>
    <p>번호 : {{selectedPost.id}}</p>
    <p>제목 : {{selectedPost.title}}</p>
    <p>내용 : {{selectedPost.content}}</p>
</div>
</template>

<script setup>
import { ref } from 'vue'
import { onBeforeRouteUpdate } from 'vue-router';

const posts = ref([
    {id:1, title: 'Post1', content: 'Content1'},
    {id:2, title: 'Post2', content: 'Content2'},
    {id:3, title: 'Post3', content: 'Content3'},
])

defineProps({
    post: Object
})

const selectedPost = ref(null)

onBeforeRouteUpdate((to) => {
    const postId = to.params.id
    console.log(postId)
    selectedPost.value = posts.value.find(post => post.id == postId)
})

</script>

<style scoped>

</style>