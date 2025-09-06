<template>
  <header>
    <h1>pinia + router 연습하기</h1>
    <nav>
      <RouterLink to="/">main</RouterLink>
    </nav>
  </header>
  <hr>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
</script>

<style scoped>
header {
  padding: 20px;
  text-align: center;
}
nav {
  margin-top: 10px;
}
</style>