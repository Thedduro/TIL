<template>
  <div>
  <h2 class="mb-4 fw-bold">영화조회</h2>
    <div v-if="loading" class="text-center my-5">
      <div class="spinner-border" role="status"><span class="visually-hidden">Loading...</span></div>
    </div>
    <div v-else-if="error" class="alert alert-danger">{{ error }}</div>
    <div v-else>
      <div v-if="movies.length" class="row row-cols-1 row-cols-md-3 g-4">
        <div class="col d-flex" v-for="m in movies" :key="m.id">
          <MovieCard :movie="m" />
        </div>
      </div>
  <div v-else class="text-center text-muted py-5">영화 데이터가 없습니다.</div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getTopRated } from '../api/tmdb'
import MovieCard from '../components/MovieCard.vue'

const movies = ref([])
const loading = ref(true)
const error = ref('')

onMounted(async () => {
  loading.value = true
  error.value = ''
  try {
    const { data } = await getTopRated(1)
    movies.value = data.results || []
  } catch (e) {
    error.value = '영화 정보를 불러오지 못했습니다.'
    alert(error.value)
  } finally {
    loading.value = false
  }
})
</script>
