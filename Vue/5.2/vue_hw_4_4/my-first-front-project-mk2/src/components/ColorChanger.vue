<template>
<input v-model="colorClass" type="text">
<p :class="colorClass">입력창에 올바른 색상 명을 입력하면 글자색이 바껴요.</p>
</template>

<script setup>
import { ref } from 'vue'
const colorClass = ref('')
</script>

<style scoped>
.red {
    color: red;
}
.blue {
    color: blue;
}
.green {
    color: green;
}
</style>