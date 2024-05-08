
<template>
    <header>
      <h1>명함 관리 페이지</h1>
    </header>
    <main>
        <p>명함을 관리하는 페이지입니다. 여기에 명함 목록이 표시됩니다.</p>
        <CreateCardForm @createCard="updateCard"/>
    </main>
    <article>
    <BusinessCard :newCard="newCard"/>
    </article>
    <footer>
    <p>&copy 2023 My Business Cards</p>
    </footer>
    </template>
    
    <script setup>
    import BusinessCard from '@/components/BusinessCard.vue';
    import CreateCardForm from '@/components/CreateCardForm.vue';
    import {ref} from 'vue'

    let newCard = ref(null)

    const updateCard = function(cardInfo) {
        newCard.value = cardInfo
    }

    </script>
    
    <style scoped>
    
    header{
      width: 325px;
      height: 100px;
      background-color: cornflowerblue;
      color: white;
      display: flex;
      justify-content: center;
      align-items: center;
      margin: 0 auto
    }
    main{
      display: flex;
      justify-content: center;
      align-items: center;
      flex-direction: column;
    }
    footer{
      width: 100%;
      height: 50px;
      background-color: rgb(245, 242, 242);
      display: flex;
      justify-content: center;
      align-items: center;
      position: fixed;
    bottom: 0;
    left: 0;
    }
    </style>
    