<template>
    <div class='singcardlist'>
        <div class='singcard'>
            <h3>앨범 제목</h3>
            <p>노래 목록 1</p>
            <p>노래 목록 2</p>
            <p>노래 목록 3</p>
        </div>
        <div class='singcard'>
            <h3>앨범 제목</h3>
            <p>노래 목록 1</p>
            <p>노래 목록 2</p>
            <p>노래 목록 3</p>
        </div>
    </div>
</template>

<script>
</script>

<style scoped>
.singcardlist {
    display: flex;
    justify-content: center;
    margin: 5px
}
.singcard {
    width: 90px;
    height: 170px;
    border: 1px solid;
    border-radius: 10px;
    padding: 10px;
    margin: 10px;
    box-shadow: 5px 3px 3px lightgreen;
    background-color: lightblue
}
p {
    color: orangered;
}
</style>