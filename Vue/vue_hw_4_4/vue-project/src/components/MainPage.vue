<template>
  <div>
    <p>이름: {{ balanceInfo.name }}</p>
    <p>잔고: {{ balanceInfo.balance }}</p>
    <RouterLink :to="{ name: 'update', params: { name: balanceInfo.name } }">
      <button>updateBalance</button>
    </RouterLink>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
defineProps({
  balanceInfo: Object
})
</script>

<style scoped>
div {
  border: 1px solid #ccc;
  padding: 10px;
  margin-bottom: 10px;
}
</style>