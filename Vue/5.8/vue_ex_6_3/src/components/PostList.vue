<template>
<h2>{{username}}이 작성한 게시글</h2>
<ol>
    <PostListItem v-for="post in posts" :post="post" :key="post.id"/>
</ol>
<hr>
<RouterView />
</template>

<script setup>
import PostListItem from '@/components/PostListItem.vue'
import {ref} from 'vue'
import { useRoute } from 'vue-router'

const posts = ref([
    {id: 1, title: 'Post1', content: 'Content1'},
    {id: 2, title: 'Post2', content: 'Content2'},
    {id: 3, title: 'Post3', content: 'Content3'},
])

const route = useRoute()
const username = ref(route.params.username)

</script>

<style scoped>

</style>