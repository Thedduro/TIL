<template>
  <div>
    <div class="input-group mb-4">
      <input v-model="keyword" @keyup.enter="onSearch" type="text" class="form-control" placeholder="영화 키워드 입력" />
      <button class="btn btn-primary" @click="onSearch">검색</button>
    </div>
    <div v-if="!searched" class="text-center text-muted py-5">
      <img src="https://cdn-icons-png.flaticon.com/512/833/833593.png" width="80" class="mb-3" />
      <div>영화 리뷰 영상을 키워드로 검색해보세요!</div>
    </div>
    <div v-else>
      <div v-if="loading" class="text-center my-5">
        <div class="spinner-border" role="status"><span class="visually-hidden">Loading...</span></div>
      </div>
      <div v-else-if="error" class="alert alert-danger">{{ error }}</div>
      <div v-else-if="items.length" class="row row-cols-1 row-cols-md-3 g-3">
        <div class="col" v-for="item in items" :key="item.id.videoId">
          <YoutubeCard :item="item" @open="open" />
        </div>
      </div>
      <div v-else class="text-center text-muted py-5">검색 결과가 없습니다.</div>
    </div>
    <YoutubeReviewModal :videoId="selectedVideoId" :visible="showModal" @close="showModal=false" />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { searchYoutube } from '../api/youtube'
import YoutubeCard from '../components/YoutubeCard.vue'
import YoutubeReviewModal from '../components/YoutubeReviewModal.vue'

const keyword = ref('')
const items = ref([])
const loading = ref(false)
const error = ref('')
const searched = ref(false)
const selectedVideoId = ref('')
const showModal = ref(false)

async function onSearch() {
  if (!keyword.value.trim()) return
  loading.value = true
  error.value = ''
  searched.value = true
  items.value = []
  try {
    const res = await searchYoutube(`${keyword.value} review`, 12)
    items.value = res.items || []
  } catch (e) {
    error.value = '검색 중 오류가 발생했습니다.'
  } finally {
    loading.value = false
  }
}

function open(item) {
  selectedVideoId.value = item.id.videoId
  showModal.value = true
}
</script>
