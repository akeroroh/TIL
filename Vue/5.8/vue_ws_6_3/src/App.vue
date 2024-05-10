<template>
  <div class="quiz-app">
    <div class="app">
      <div class="app-header">
        <h1>Quiz 퀴즈</h1>
      </div>
      <div class="app-description">
        <p>여기는 퀴즈의 나라! 놀라운 퀴즈들이 기다리고 있어요. 지금 바로 도전해보세요!</p>
      </div>
    </div>
    <nav class="app-nav">
      <RouterLink :to="{name: 'home'}" class="nav-link">Home</RouterLink>   | 
      <RouterLink :to="{name: 'quiz'}" class="nav-link">Quiz</RouterLink>   |
    </nav>
  </div>
  
  <RouterView />
</template>

<script setuo>
import { RouterLink, RouterView } from 'vue-router';
</script>

<style scoped>
.quiz-app{
  width: 650px;
  background-color: rgb(238, 234, 234);
  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin: 0 auto;
  margin-bottom: 80px
}

.app{
  border: 1px solid lightgray;
  width: 100%;
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
  border-radius: 10px;
  background-color: white;
  overflow: hidden;
  margin: 0px;
}

.app-header{
  background-color: orange;
  width: 100%;
  text-align: center;
  margin: 0;
  color: white;
  padding: 8px 0px;
}

.app-description{
  text-align: center;
  padding: 15px
}

.app-nav{
  width: 100%;
  background-color: black;
  color: white;
  text-decoration-line: none;
  display: flex;
  justify-content: center;
  padding: 10px 0px;
  margin: 30px 0px 0px 0px
}

.nav-link{
  color: white;
  text-decoration-line: none;
}

</style>
