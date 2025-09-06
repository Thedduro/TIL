import { createRouter, createWebHistory } from 'vue-router'
import Mainview from '@/views/Mainview.vue'
import UpdateView from '@/views/UpdateView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: Mainview,
    },
    {
      // :name 부분은 동적으로 변하는 파라미터를 의미합니다.
      path: '/update/:name',
      name: 'update',
      component: UpdateView,
    },
  ],
})

export default router
