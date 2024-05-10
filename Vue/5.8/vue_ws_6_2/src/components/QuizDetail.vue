<template>
    <div class="quizcard">
        <p style="font-weight:bold">{{quiz.pk}}번 문제.{{quiz.question}}</p>
        <p>정답 입력</p>
        <input class="inputcard" type="text">
    </div>
</template>

<script setup>
defineProps({
    quiz: Object,
})
</script>

<style scoped>
.quizcard{
    background-color: rgb(238, 234, 234);
    border-radius: 10px;
    border: 1px solid lightgray;
    padding: 20px;
    margin: 15px;
    box-shadow: 2px 2px 2px 2px lightgray
}
.inputcard{
    width: 100%;
    height: 30px;
    border: 1px solid black;
    border-radius: 5px
}
</style>