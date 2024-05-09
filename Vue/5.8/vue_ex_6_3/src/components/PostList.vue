<template>
<h2>이 작성한 게시글</h2>
<ol>
    <PostListItem v-for="post in posts" :post="post" :key="post.id"/>
</ol>
<hr>
</template>

<script setup>
import PostListItem from '@/components/PostListItem.vue'
import {ref} from 'vue'

let id = 0
const posts = ref([
    {id:id++, title: 'Post1', content: 'Content1'},
    {id:id++, title: 'Post2', content: 'Content2'},
    {id:id++, title: 'Post3', content: 'Content3'},
])
</script>

<style scoped>

</style>