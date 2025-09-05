<template>
  <div class="card h-100 shadow-sm hover-pointer" @click="$emit('open', item)">
    <img :src="item.snippet.thumbnails.medium.url" class="card-img-top" :alt="item.snippet.title" style="object-fit:cover; height:180px; background:#222;" />
    <div class="card-body">
      <div class="fw-bold mb-1 line-clamp-2">{{ item.snippet.title }}</div>
      <div class="text-secondary small mb-1">{{ item.snippet.channelTitle }}</div>
      <div class="text-muted small">{{ item.snippet.publishedAt.slice(0,10) }}</div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({ item: Object })
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
  min-height: 2.6em;
}
.hover-pointer { cursor: pointer; }
</style>
