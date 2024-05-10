<template>
<div @submit.prevent="createQuiz" class="quizcreateform">
    <p>{{}}번 문제</p>
    <h2>정답 확인</h2>
    <div>
        <h4>정답입니다!</h4>
        <p>나의 제출 답안: {{}}</p>
        <p>정답: {{}}</p>
    </div>
</div>
</template>

<script setup>

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

</style>