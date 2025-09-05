<template>
  <div>
    <div v-if="loading" class="text-center my-5">
      <div class="spinner-border" role="status"><span class="visually-hidden">Loading...</span></div>
    </div>
    <div v-else-if="error" class="alert alert-danger">{{ error }}</div>
    <div v-else-if="movie">
      <MovieDetailInfo :movie="movie" @open-trailer="showTrailer = true" />
      <YoutubeTrailerModal :query="movie?.title" :visible="showTrailer" @close="showTrailer = false" />
    </div>
  </div>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue'
import { getMovieDetail } from '../api/tmdb'
import MovieDetailInfo from '../components/MovieDetailInfo.vue'
import YoutubeTrailerModal from '../components/YoutubeTrailerModal.vue'
const props = defineProps({ movieId: [String, Number] })
const movie = ref(null)
const loading = ref(true)
const error = ref('')
const showTrailer = ref(false)

async function fetchDetail(id) {
  loading.value = true
  error.value = ''
  try {
    const { data } = await getMovieDetail(id)
    movie.value = data
  } catch (e) {
    error.value = '영화 상세 정보를 불러오지 못했습니다.'
  } finally {
    loading.value = false
  }
}

watch(() => props.movieId, (id) => {
  if (id) fetchDetail(id)
}, { immediate: true })

onMounted(() => {
  if (props.movieId) fetchDetail(props.movieId)
})
</script>
