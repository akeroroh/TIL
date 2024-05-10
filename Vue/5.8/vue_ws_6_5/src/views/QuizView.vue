<template>
    <QuizCreate @changeQuiz="changeQuiz" @updateQuiz="updateQuiz" />
    <div class="quizlist">
        <QuizDetail v-for="quiz in quizListSorted" :quiz="quiz" :key="quiz.pk"/>
    </div>
    </template>
    
    <script setup>
    import {ref, computed} from 'vue'
    import {onBeforeRouteLeave} from 'vue-router'
    import QuizDetail from '../components/QuizDetail.vue';
    import QuizCreate from '../components/QuizCreate.vue';
    
    let pk = 1
    const quizs = ref([
        {pk: pk++, question: '\'Python\' 웹 프레임워크 중 하나로, 마이크로 웹 프레임워크로 빠른 개발을 지원하는 것은?', answer: 'flask'},
        {pk: pk++, question: 'HTML에서 텍스트 입력란을 만드는 데 사용되는 요소는?', answer: 'input'},
        {pk: pk++, question: '웹 애플리케이션에서 클라이언트의 데이터를 서버로 전송할 때 주로 사용되는 HTTP 메서드는?', answer: 'post'},
        {pk: pk++, question: 'Python의 가상 환경을 만들어 프로젝트 별로 라이브러리 의존성을 격리시키는 명령어는?', answer: 'virtualenv'},
        {pk: pk++, question: '웹 애플리케이션을 개발할 때, 사용자의 브라우저에 보여지는 부분을 렌더링하는 언어는 무엇인가요?', answer: 'html'},
    ])
    
    const updateQuiz = function(quizItem) {
        quizItem.pk = pk++
        quizs.value.push(quizItem)
    }
    
    const quizListSorted = computed(() => {
        return [...quizs.value].sort((a, b) => b.pk - a.pk);
    });

    const isWriting = ref(false)
    const changeQuiz = function(quiz) {
        if (!quiz.question || !quiz.answer) {
            isWriting.value = true
        }
    }

    onBeforeRouteLeave((to, from) => {
        console.log(isWriting.value)
        if (isWriting.value === true) {
            const answer = window.confirm('작성중이던 문제가 있습니다. 다른 경로로 이동시 작성중이던 내용은 소멸됩니다. 이동하시겠습니까?')
            if (answer === true) {
                return true
            } else {
                return false
            }
        } 
    })
    </script>
    
    <style scoped>
    .quizlist{
        display: flex;
        justify-content: center;
        flex-direction: column;
    }
    </style>