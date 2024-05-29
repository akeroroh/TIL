<template>
    <div>
        <P>{{ todo.work }}</P>
        <P>{{ todo.content }}</P>
        <P>{{ todo.is_completed }}</P>
        <P>{{ todo.created_at }}</P>
        <hr>
    </div>
</template>

<script setup>
import {defineProps} from 'vue'
defineProps({
    todo: Object
})
</script>

<style scoped>

</style>