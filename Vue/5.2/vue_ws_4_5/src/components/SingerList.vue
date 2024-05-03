<template>

    <div class='singercontainer'>

        <div v-for='_ in singers'>
            <SingerDetail/>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
const singers = ref([
    {name: 'adele'},
    {name: 'marron 5'},
    {name: 'Dua Lipa'},
])
import SingerDetail from '@/components/singers/SingerDetail.vue'
</script>

<style scoped>
h1 {
    color: orangered
}

</style>
