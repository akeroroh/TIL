<template>
    <h2>보유 명함 목록</h2>
    <div v-if="businessCards.length !== 0">
        <div class='info'>
            <p>현재 보유중인 명함 수 : {{businessCards.length}}</p>
        </div>
        <container>
            <div class="card" v-for="businessCard in businessCards" :key="businessCard.id">
                <div class="info">
                    <h4>이름 : {{businessCard.name}}</h4>
                    <p>직함 : {{businessCard.title}}</p>
                    <button @click="deleteCardFunc(businessCard)">명함 삭제</button>
                </div>
            </div>
        </container>
    </div>
    <div v-else class='info'>
        <p>명함이 없습니다. 새로운 명함을 추가해 주세요.</p>
    </div>
</template>

<script setup>
defineProps({
    businessCards: Array,
})

const emit = defineEmits(['deleteCardFunc'])
const deleteCardFunc = function(businessCard) {
    emit('deleteCardFunc', businessCard)
}
</script>

<style scoped>
h2{
    text-align: center;
}
.card {
    border: 1px solid lightgray;
    width: 400px;
    height: 125px;
    background-color: #f0f0f0;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 10px;
    flex-direction: column;
    padding: 10px
}
container{
    display: flex;
    flex-wrap: wrap;
    justify-content: center
}
.info{
    text-align: center;
    padding: 3px
}
button{
    margin: 7px
}
</style>