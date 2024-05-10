<template>
<form @change="changeQuiz" @submit.prevent="createQuiz" class="quizcreateform">
    <h2>퀴즈 생성</h2>
    <p style="margin-bottom: 2px">문제</p>
    <input v-model="question" class="inputquestion" type="text">
    <p style="margin-bottom: 2px">정답</p>
    <input v-model="answer" class="inputanswer" type="text">
    <input class="quizinput" type="submit" value="퀴즈 생성">
</form>
</template>

<script setup>
import {ref} from 'vue'

const emit = defineEmits(['updateQuiz', 'changeQuiz'])
const question = ref('')
const answer = ref('')

const createQuiz = function() {
    const quizItem = {
        question: question.value,
        answer: answer.value
    }
    emit('updateQuiz', quizItem)
    question.value = ''
    answer.value = ''
}

const changeQuiz = function() {
    const quiz = {
        question: question.value,
        answer: answer.value
    }
    emit('changeQuiz', quiz)
}
</script>

<style scoped>
.quizcreateform{
    width: 650px;
    background-color: rgb(238, 234, 234);
    border: 1px solid rgb(238, 234, 234);
    border-radius: 10px;
    margin: 0 auto;
    padding: 20px;
    display: flex;
    flex-direction: column;
    margin-bottom: 30px;
    box-shadow: 2px 2px 2px 2px lightgray
}
.inputquestion{
    width: 99%;
    height: 80px;
    border: 1px solid gray;
    border-radius: 5px;
    margin-top: 3px
}
.inputanswer{
    width: 99%;
    height: 30px;
    border: 1px solid gray;
    border-radius: 5px;
    margin-top: 3px;
    margin-bottom: 30px
}
.quizinput{
    background-color: rgb(49, 144, 255);
    color: white;
    width: 100%;
    border: 1px solid rgb(49, 144, 255);
    border-radius: 5px;
    height: 30px;
}
</style>