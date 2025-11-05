import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
      path: '/',
      name: 'list',
      component: () => import('../views/TaskListView.vue')
  }
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export default router
