<template>
    <div class='card'>
        <h1 style="text-align: center">가수 이름</h1>
        <img style="border-radius: 70%" width='200' src="@/assets/singer.jpg" alt="#">
        <p style="text-align: center">가수 소개글</p>
        <SingerAlbum/>
    </div>
</template>

<script setup>
    import SingerAlbum from '@/components/singers/SingerAlbum.vue'
</script>

<style scoped>
.card {
    display: inline-block;
    width: 40%;
    margin: 20px;
    padding: 10px 30px;
    border: 1px solid;
    text-align: center
}
</style>
