import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useProductStore = defineStore('product', () => {
  const products = ref([
    { id: 1, title: 'Product 1', body: 'quia et suscipit suscipit recusandae' },
    { id: 2, title: 'Product 2', body: 'quo iure voluptatem occaecati omnis' },
    { id: 3, title: 'Product 3', body: 'repudiandae veniam quaerat sunt' }
  ])

  const productCount = computed(() => products.value.length)

  const deleteProduct = function (productId) {
    const index = products.value.findIndex(product => product.id === productId)
    if (index !== -1) {
      products.value.splice(index, 1)
    }
  }

  axios({
    method: 'get',
    url: 'https://jsonplaceholder.typicode.com/posts'
  })
    .then((response) => {
      products.value = response.data.map(item => ({
        id: item.id,
        title: item.title,
        body: item.body
      }))
      console.log(response)
    })
  return { products, productCount, deleteProduct }
})
