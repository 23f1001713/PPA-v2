import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    component: () => import('@/views/shared/LandingPage.vue')
  },
  {
    path: '/login',
    component: () => import('@/views/auth/Login.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router