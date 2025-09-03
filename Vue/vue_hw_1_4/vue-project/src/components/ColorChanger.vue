<template>
  <div>
    <input v-model="colorClass" placeholder="색상명을 입력하세요 (red, blue, green)" />
    <p :class="colorClass">입력창에 올바른 색상 명을 입력하면 글자색이 바껴요.</p>   
  </div>
</template>

<script setup>
import { ref } from 'vue';

const colorClass = ref('');
</script>


<style scoped>
  .red {
    color: red;
  }
  .blue {
    color: blue;
  }
  .green {
    color: green;
  }
</style>