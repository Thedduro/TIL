<script setup>
import { ref } from 'vue'
import ChildPage from './ChildPage.vue' // 1. ChildPage 컴포넌트를 가져옵니다.

const children = ref([
  { name: '김하나', age: 30 },
  { name: '김두리', age: 20 },
  { name: '김서이', age: 10 },
])
</script>

<template>
  <div style="border: 1px solid black; padding: 20px;">
    <h1>부모 페이지입니다.</h1>
    <ChildPage 
      v-for="child in children" 
      :key="child.name"
      :child-data="child" 
    />
  </div>
</template>