<template>
    <h1>부모 페이지입니다.</h1>
    <ChildPage :children="children" @give-me-allowance="updateBalance"/>
    </template>
    
    <script setup>
    import ChildPage from '@/components/ChildPage.vue'
    import {ref} from 'vue'
    const children = ref([
        {name: '김하나', age: 30, balance: 100000},
        {name: '김두리', age: 20, balance: 10000},
        {name: '김서이', age: 10, balance: 1000},
    ])

    const updateBalance = function(child) {
        const index = children.value.findIndex(item => item === child);
        if (index !== -1) {
            children.value[index].balance += 1000;
        }
    }
    
    </script>
    
    <style scoped>
    
    </style>