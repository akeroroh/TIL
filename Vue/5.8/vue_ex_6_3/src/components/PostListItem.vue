<template>
<li @click="routeUpdate">
    <RouterLink :to="{name:'post-detail', params: {'username': username, 'id': post.id }}" :post='post'>제목: {{ post.title }}</RouterLink>
</li>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'

defineProps({
    post: Object,
})

const route = useRoute()
const router = useRouter()
const username = ref(route.params.username)

const routeUpdate = function() {
    router.push({name: 'post-detail', params: {'username': username.value,'id': post.id}})
}

</script>

<style scoped>

</style>