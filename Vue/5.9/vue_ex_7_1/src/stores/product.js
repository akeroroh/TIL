import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useProductStore = defineStore('product', () => {
    let id = 0
    const products = ref([
        {id: id++,title: 'Product 1', body: 'quia et suscipit suscipit recusandae'},
        {id: id++,title: 'Product 2', body: 'quo iure voluptatem occaecati omnis'},
        {id: id++,title: 'Product 3', body: 'repudiandae veniam quaerat sunt'},
    ])
    return {products}
})
