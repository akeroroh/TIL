<template>
<div class="quizcreateform">
    <p style="margin-bottom:0px; text-align:center; margin:0px" class="text-align: center">{{questionpk}}번 문제</p>
    <h2 style="margin-bottom: 10px, ">정답 확인</h2>
    <div class="answerzone">
        <h4 :class="{ 'correct-answer': iscorrectAnswer, 'wrong-answer': !iscorrectAnswer }">{{iscorrectAnswer ? '정답입니다!': '오답입니다.'}}</h4>
        <p :class="{ 'correct-answer': iscorrectAnswer, 'wrong-answer': !iscorrectAnswer }">나의 제출 답안: {{userAnswer}}</p>
        <p>정답: {{answer}}</p>
    </div>
</div>
</template>

<script setup>
import {useRouter, useRoute} from 'vue-router'
import {computed} from 'vue'

const router = useRouter()
const route = useRoute()

const questionpk = route.params.pk
const userAnswer = route.query.useranswer
const answer = route.params.answer

const iscorrectAnswer = computed(() => {
    return userAnswer === answer
})
</script>

<style scoped>
.quizcreateform{
    width: 650px;
    background-color: rgb(238, 234, 234);
    border: 2px solid lightgray;
    border-radius: 10px;
    margin: 0 auto;
    padding: 20px;
    display: flex;
    flex-direction: column;
    margin-bottom: 30px;
    box-shadow: 2px 2px 2px 2px lightgray
}
.answerzone{
    background-color: white;
    border: 2px solid lightgray;
    border-radius: 10px;
    padding: 15px
}
h2{
    margin-top: 0px;
    text-align: center;
    font-weight: bold
}
.correct-answer {
  color: green;
}

.wrong-answer {
  color: red;
}

</style>