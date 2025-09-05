<template>
  <div v-if="visible" class="modal fade show d-block" tabindex="-1" style="background:rgba(0,0,0,0.5);">
    <div class="modal-dialog modal-lg modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">리뷰 영상</h5>
          <button type="button" class="btn-close" @click="closeModal"></button>
        </div>
        <div class="modal-body p-0" style="min-height:400px;">
          <iframe
            v-if="videoId"
            :src="`https://www.youtube.com/embed/${videoId}?autoplay=1`"
            width="100%" height="400" frameborder="0" allowfullscreen allow="autoplay; encrypted-media">
          </iframe>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { watch } from 'vue'
const props = defineProps({ videoId: String, visible: Boolean })
const emit = defineEmits(['close'])
let lastVideoId = ''

function closeModal() {
  emit('close')
  lastVideoId = ''
}

watch(() => props.visible, (v) => {
  if (!v) lastVideoId = ''
})
</script>

<style scoped>
.modal { display: block; }
</style>
