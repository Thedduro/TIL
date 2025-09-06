<template>
  <div class="parent-container">
    <h3>부모 컴포넌트</h3>
    <p>{{ family.father }}</p>
    <p>{{ family.mother }}</p>
    <ChildPage 
      v-for="child in family.children" 
      :key="child.name"
      :child-info="child"
    />
  </div>
</template>

<script setup>
import ChildPage from '@/components/ChildPage.vue';

defineProps({
  family: Object
})
</script>

<style scoped>
.parent-container {
  border: 1px solid #000;
  padding: 20px;
  margin-top: 20px;
  text-align: center;
  background-color:gainsboro;
}
</style>