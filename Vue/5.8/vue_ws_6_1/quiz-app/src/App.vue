
<template>
  <body>
    <div class="container">
      <div class="titlecard">
        <h1 class="titletitle">Quiz 퀴즈</h1>
        <p>여기는 퀴즈의 나라! 놀라운 퀴즈들이 기다리고 있어요. 지금 바로 도전해보세요!</p>
      </div>
      <div class="homebutton">
        <RouterLink style="text-decoration-line: none; color:white":to="{name: 'homeview'}">Home</RouterLink>
        <span> | </span>
      </div>
    </div>
  </body>
  <div class="homeview">
    <RouterView/>
  </div>
    
</template>

<script setup>
import HomeView from '@/views/HomeView.vue'
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>


body{
  margin: 0;
  padding: 50px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.container{
  background-color: rgb(238, 234, 234);
  padding: 10px;
  margin: 0 auto;
}

.titlecard{
  border: 1px solid lightgray;
  width: 600px;
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
  border-radius: 10px;
  margin: 0 auto;
  background-color: white;
  overflow: hidden
}

.titletitle{
  background-color: orange;
  width: 100%;
  text-align: center;
  margin: 0;
  color: white;
  padding: 8px 0px;
}

.homebutton{
  width: 600px;
  background-color: black;
  color: white;
  text-decoration-line: none;
  display: flex;
  justify-content: center;
  padding: 10px 0px;
  margin: 20px 0px 0px 0px
}

.homeview{
  margin: 0;
  padding: 50px;
}
</style>
