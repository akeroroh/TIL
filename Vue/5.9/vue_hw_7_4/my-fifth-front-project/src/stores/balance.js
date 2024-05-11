import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import {useRoute} from 'vue-router'

export const useBalanceStore = defineStore('balance', () => {
    const balances = ref([
        {
        name: '김하나',
        balance: 100000
        },
        {
        name: '김두리',
        balance: 10000
        },
        {
        name: '김서이',
        balance: 100
        },
    ])
    
    const route = useRoute()

    const correctBalance = computed(() => {
        const name = route.params.name
        const balance = balances.value.find((balance) => balance.name === name )
        return balance
    })

    const plusBalance = function() {
        const name = route.params.name
        balances.value = balances.value.map((balance) => {
            if (balance.name === name) {
                balance.balance += 1000
            }
            return balance
        })
    }
 
    return { balances, correctBalance, route, plusBalance }
})
