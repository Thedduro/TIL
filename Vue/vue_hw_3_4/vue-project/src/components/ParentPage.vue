<script setup>
import { ref } from 'vue'
import ChildPage from './ChildPage.vue'

const children = ref([
  { name: '김하나', age: 30, balance: 100000 },
  { name: '김두리', age: 20, balance: 10000 },
  { name: '김서이', age: 10, balance: 1000 },
])

// 1. 자식에게서 받은 객체의 balance를 1000 증가시키는 함수
const updateBalance = (childToUpdate) => {
  // children 배열에서 전달받은 자식과 이름이 같은 자식을 찾아 잔액을 업데이트
  const child = children.value.find(c => c.name === childToUpdate.name)
  if (child) {
    child.balance += 1000
  }
}
</script>

<template>
  <div style="border: 1px solid black; padding: 20px;">
    <h1>부모 페이지입니다.</h1>
    <ChildPage 
      v-for="child in children" 
      :key="child.name"
      :child-data="child"
      @give-me-allowance="updateBalance(child)"
    />
  </div>
</template>