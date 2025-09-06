<template>
  <div>
    <h4>자식 페이지</h4>
    <p>{{ childInfo.name }}</p>
  </div>
</template>

<script setup>
defineProps({
  childInfo: Object
})
</script>

<style scoped>
div {
  border: 1px solid #ccc;
  padding: 10px;
  margin-top: 10px;
  text-align: center;
  background-color: white;
}

</style>