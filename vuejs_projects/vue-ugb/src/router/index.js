import { createRouter, createWebHistory } from 'vue-router'
import ClientsView from '@/views/ClientsView.vue'

const routes = [
  {
    path: '/clients',
    component: ClientsView,
    name: 'clients'
  }
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routes,
})

export default router
