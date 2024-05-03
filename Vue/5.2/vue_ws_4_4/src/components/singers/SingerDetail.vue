<template>
    <div class='row'>
        <div class='card col'>
            <h1 style="text-align: center">가수 이름</h1>
            <div class='image-container'>
                <img style="border-radius: 70%" width='200' src="@/assets/singer.jpg" alt="#">
            </div>
            <p style="text-align: center">가수 소개글</p>
        </div>
        <div class='card col'>
            <h1 style="text-align: center">가수 이름</h1>
            <div class='image-container'>
                <img style="border-radius: 70%" width='200' src="@/assets/singer.jpg" alt="#">
            </div>
            <p style="text-align: center">가수 소개글</p>
        </div>
    </div>
</template>

<style scoped>
.card {
    display: inline-block;
    width: 40%;
    margin: 20px
}
.row {
    display: flex;
    justify-content: space-around
}
.col {
    border: 1px solid;
    text-align: center
}
img-container {
    display: flex;
    justify-content: center;
           
}
</style>