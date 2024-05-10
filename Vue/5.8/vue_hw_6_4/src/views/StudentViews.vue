<template>
<h1>학생 상세 정보 목록 입니다.</h1>
<a @click="gostudent(student)" v-for="student in students">
    <p>{{ student.name }} 학생 정보 보기</p>
</a>
</template>

<script setup>
import {ref} from 'vue'
import {useRouter} from 'vue-router'
const students = ref([
    {name: '김하나'},
    {name: '김두리'},
    {name: '김서이'},
])
const router = useRouter()
const gostudent = function(student) {
    router.push({name: 'studentdetail', params:{name: student.name}})
}

</script>

<style scoped>

</style>