<template>
    <div  class="maincard">
        <h2>부모 컴포넌트</h2>
        <p>{{family.father}}</p>
        <p>{{family.mother}}</p>
        <ChildPage v-for="children in family.children" :id=children.id :children="children"/>
    </div>
</template>

<script setup>
import ChildPage from '@/components/ChildPage.vue'
defineProps({
    family: Object,
})
</script>

<style scoped>
.maincard{
    background-color: #F9F9F9;
    margin: 10px;
    border: 2px solid lightgray;
    text-align: center;
    padding: 10px
}
</style>