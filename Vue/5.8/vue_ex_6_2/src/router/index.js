import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import AboutView from '@/views/AboutView.vue'
import UserView from '@/views/UserView.vue'
import { ref } from 'vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView
    },
    {
      path: '/user/:username',
      name: 'user',
      component: UserView,
      beforeEnter: (to) => {
        const requestedUsername = to.params.username
        if (requestedUsername !== 'admin') {
          window.alert('현재 프로필 페이지는 admin만 접근 가능합니다.')
          return {name: 'home'}
        }
      }
    }
  ]
})

export default router
