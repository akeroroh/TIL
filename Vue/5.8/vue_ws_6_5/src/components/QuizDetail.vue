<template>
    <div class="quizcard">
      <p style="font-weight:bold">{{ quiz.pk }}번 문제.{{ quiz.question }}</p>
      <p>정답 입력</p>
      <input @keyup.enter="submitAnswer(quiz)" v-model="useranswer" class="inputcard" type="text" id="{{ quiz.pk }}">
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  defineProps({
    quiz: Object,
  })
  const useranswer = ref('')
  const router = useRouter()

  const submitAnswer = (quiz) => {
    if (window.confirm(`${useranswer.value}을/를 답안으로 제출합니다. 확실합니까?`)) {
      router.push({
        name: 'answer',
        params: { pk: quiz.pk, answer: quiz.answer },
        query: { useranswer: useranswer.value },
      })
    } else {
      useranswer.value = ''
    }
  }


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