import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useProductStore = defineStore('counter', () => {
    const productList = ref([
        {name: '상품 1', imagePath: 'src/assets/product1.png', price: 10000, isFavorite: false},
        {name: '상품 2', imagePath: 'src/assets/product2.png', price: 20000, isFavorite: false},
        {name: '상품 3', imagePath: 'src/assets/product3.png', price: 30000, isFavorite: false},
        {name: '상품 4', imagePath: 'src/assets/product4.png', price: 40000, isFavorite: false},
    ])

    const updatefavorite = function(productName) {
       productList.value = productList.value.map((product) => {
        if(product.name === productName) {
            product.isFavorite = !product.isFavorite
        }
        return product
       }) 
    }

    const countFavorite = computed(() => {
        const yesFavorite = productList.value.filter((product) => product.isFavorite)
        return yesFavorite.length
    })
    return { productList, updatefavorite, countFavorite }
})