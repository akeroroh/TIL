<template>
    <div>
        <h1>pinia 연습하기</h1>
    </div>
    <div class="maincard">
        <ParentPage v-for="family in store.familyInfo" :key=family.id :family="family"/>
    </div>
</template>

<script setup>
import ParentPage from '@/components/ParentPage.vue'
import {useFamilyStore} from '@/stores/family'

const store = useFamilyStore()
</script>

<style scoped>
</style>