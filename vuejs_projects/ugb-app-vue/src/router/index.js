import { createRouter, createWebHistory } from 'vue-router'
import ClientsView from '@/views/ClientsView.vue'
import AboutView from '@/views/AboutView.vue'

const routes = [
  {
    path: '/clients',
    component: ClientsView,
    name: 'clients'
  },
  {
    path: '/about',
    component: AboutView,
    name: 'about'
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routes,
})

export default router
