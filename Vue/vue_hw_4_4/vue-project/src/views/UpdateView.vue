<template>
  <div>
    <h2>데이터 수정 페이지</h2>
    <div v-if="person">
      <p>이름: {{ person.name }}</p>
      <p>잔고: {{ person.balance }}</p>
      <button @click="store.updateBalance(person.name)">+</button>
    </div>
    <div v-else>
      <p>데이터를 찾을 수 없습니다.</p>
    </div>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { useBalanceStore } from '@/stores/balance'

const route = useRoute()
const store = useBalanceStore()

// URL의 :name 파라미터 값을 가져옵니다.
const name = route.params.name
// Pinia getter를 사용해 해당 이름의 사람 정보를 찾습니다.
const person = store.getBalanceByName(name)
</script>