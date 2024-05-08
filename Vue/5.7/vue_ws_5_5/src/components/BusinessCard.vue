<template>
    <businessCardDetail :businessCards="businessCards" @delete-card-func="deleteCard"/>
    </template>
    
    <script setup>
    import businessCardDetail from '@/components/businessCardDetail.vue';
    import { ref, watch } from 'vue'
    let id = 0
    const businessCards = ref([
        {id: id++, name: '일론 머스크', title: '테슬라 테크노킹'},
        {id: id++, name: '래리 엘리슨', title: '오라클 창업주'},
        {id: id++, name: '빌 게이츠', title: '마이크로소프트 공동창업주'},
        {id: id++, name: '래리 페이지', title: '구글 공동창업주'},
        {id: id++, name: '세르게이 브린', title: '구글 공동창업주'},
    ])

    const deleteCard = function(businessCard) {
        const index = businessCards.value.indexOf(businessCard);
        if (index !== -1) {
            businessCards.value.splice(index, 1);
        }
    }

    const props = defineProps({
        newCard: Object
    })
    watch(() => props.newCard, (card) => businessCards.value.push(card))
    </script>
    
    <style lang="scss" scoped>
    
    </style>