import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue'),
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },
    {
      path: '/categories',
      name: 'categories',
      component: () => import('../views/CategoryView.vue'),
      children: [
        {
          path: '',
          name: 'list-categories',
          component: () => import('@/components/ListCategory.vue'),
        },
        {
          path: 'new',
          name: 'new-category',
          component: () => import('@/components/forms/CategoryForm.vue'),
        },
        {
          path: 'edit/:id',
          name: 'edit-category',
          component: () => import('@/components/forms/CategoryForm.vue'),
        },
      ],
    },
  ],
})

export default router
