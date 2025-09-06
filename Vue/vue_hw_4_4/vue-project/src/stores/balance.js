// src/stores/balance.js
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useBalanceStore = defineStore('balance', () => {
  // 1. State: 관리할 데이터
  const balances = ref([
    { name: '김하나', balance: 100000 },
    { name: '김두리', balance: 10000 },
    { name: '김서이', balance: 100 },
  ])

  // 2. Getters: state를 기반으로 계산된 값을 반환하는 함수
  const getBalanceByName = computed(() => {
    return (name) => {
      return balances.value.find((item) => item.name === name)
    }
  })

  // 3. Actions: state를 변경하는 메서드
  const updateBalance = (name) => {
    const person = balances.value.find((item) => item.name === name)
    if (person) {
      person.balance += 1000
    }
  }

  return { balances, getBalanceByName, updateBalance }
})