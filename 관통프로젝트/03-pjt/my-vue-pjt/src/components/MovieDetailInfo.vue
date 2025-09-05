<template>
  <div class="row g-4 align-items-start">
    <div class="col-md-4 text-center">
      <img :src="posterUrl" :alt="movie.title" class="img-fluid rounded shadow" style="max-height:500px; object-fit:cover; background:#222;" />
    </div>
    <div class="col-md-8">
      <h2 class="fw-bold mb-2">
        {{ movie.title }}
        <small class="text-muted">({{ movie.release_date ? movie.release_date.slice(0,4) : '' }})</small>
      </h2>
      <div class="mb-2">
        <span class="badge bg-primary me-2">★ {{ movie.vote_average }}</span>
        <span class="badge bg-secondary me-2">{{ movie.runtime }}분</span>
        <span v-for="g in movie.genres" :key="g.id" class="badge bg-info text-dark me-1">{{ g.name }}</span>
      </div>
      <div class="mb-3 text-secondary">{{ movie.overview }}</div>
      <div class="mb-2"><strong>개봉일:</strong> {{ movie.release_date }}</div>
      <button class="btn btn-danger" @click="$emit('open-trailer')">공식 예고편</button>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { getImageUrl } from '../api/tmdb'
const props = defineProps({
  movie: { type: Object, required: true }
})
const placeholder = 'https://via.placeholder.com/500x750?text=No+Image'
const posterUrl = computed(() =>
  props.movie.poster_path ? getImageUrl(props.movie.poster_path) : placeholder
)
</script>

<style scoped>
.img-fluid { max-width: 100%; height: auto; }
</style>
