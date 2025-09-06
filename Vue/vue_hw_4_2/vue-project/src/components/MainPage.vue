<template>
  <div class="container">
    <h1>pinia 연습하기</h1>
    <ParentPage 
      v-for="family in store.familyInfo" 
      :key="family.familyName"
      :family="family"
    />
  </div>
</template>

<script setup>
import ParentPage from '@/components/ParentPage.vue';
import { useFamilyStore } from '@/stores/family';

const store = useFamilyStore()
</script>

<style scoped>
.container {
  max-width: 800px; 
  width: 100%;
}

h1 {
  margin: 0; /* h1의 기본 마진 제거 */
  padding-block: 1rem; /* 위아래 여백 추가 */
}
</style>