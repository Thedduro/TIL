<template>
  <router-link :to="`/${movie.id}`" class="text-decoration-none text-dark w-100">
    <div class="card h-100 shadow-sm">
      <img
        :src="posterUrl"
        class="card-img-top"
        :alt="movie.title"
        style="object-fit:cover; height:400px; background:#222;"
        @error="onImgError"
      />
      <div class="card-body">
        <div class="d-flex justify-content-between align-items-center mb-2">
          <span class="fw-bold fs-5">{{ movie.title }}</span>
          <span class="badge bg-primary ms-2">★ {{ movie.vote_average }}</span>
        </div>
        <div class="card-text line-clamp text-secondary small">{{ movie.overview }}</div>
      </div>
    </div>
  </router-link>
</template>

<script setup>
import { ref, computed } from 'vue'
import { getImageUrl } from '../api/tmdb'
const props = defineProps({
  movie: {
    type: Object,
    required: true,
  },
})
const placeholder = 'https://via.placeholder.com/500x750?text=No+Image'
const posterUrl = computed(() =>
  props.movie.poster_path ? getImageUrl(props.movie.poster_path) : placeholder
)
function onImgError(e) {
  e.target.src = placeholder
}
</script>

<style scoped>
.line-clamp {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
  min-height: 4.2em;
  font-family: 'Malgun Gothic', 'Apple SD Gothic Neo', sans-serif;
}
</style>
