<template>
  <div v-if="visible" class="modal fade show d-block" tabindex="-1" style="background:rgba(0,0,0,0.5);">
    <div class="modal-dialog modal-lg modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">공식 예고편</h5>
          <button type="button" class="btn-close" @click="closeModal"></button>
        </div>
        <div class="modal-body p-0" style="min-height:400px;">
          <div v-if="loading" class="text-center py-5">
            <div class="spinner-border" role="status"><span class="visually-hidden">Loading...</span></div>
          </div>
          <div v-else-if="videoId">
            <iframe
              :src="`https://www.youtube.com/embed/${videoId}?autoplay=1`"
              width="100%" height="400" frameborder="0" allowfullscreen allow="autoplay; encrypted-media">
            </iframe>
          </div>
          <div v-else class="text-center py-5 text-muted">예고편을 찾을 수 없습니다.</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { searchYoutube } from '../api/youtube'
const props = defineProps({
  query: String,
  visible: Boolean
})
const emit = defineEmits(['close'])
const videoId = ref('')
const loading = ref(false)

function closeModal() {
  emit('close')
  videoId.value = '' // 재생 중지
}

watch(() => props.visible, async (v) => {
  if (v && props.query) {
    loading.value = true
    videoId.value = ''
    try {
      const res = await searchYoutube(`${props.query} trailer`, 1)
      videoId.value = res.items?.[0]?.id?.videoId || ''
    } catch {
      videoId.value = ''
    } finally {
      loading.value = false
    }
  } else {
    videoId.value = ''
  }
})
</script>

<style scoped>
.modal { display: block; }
</style>
