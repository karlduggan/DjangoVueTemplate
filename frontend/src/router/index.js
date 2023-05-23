// src/router/index.js

import { createRouter, createWebHistory } from 'vue-router';
import LandingPage from "../views/LandingPage";
import AuthenticationPage from "../views/AuthenticationPage";
import DashboardPage from "../views/DashboardPage";

const routes = [
  {
    path: '/',
    name: 'Home',
    component: LandingPage,
  },
  {
    path: '/login',
    name: 'login',
    component: AuthenticationPage,
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: DashboardPage,
    meta: {
      requiresAuth: true, // Add this meta field to indicate that authentication is required
    },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  const isAuthenticated = localStorage.getItem('token'); // Retrieve the authentication token

  if (to.meta.requiresAuth && !isAuthenticated) {
    next('/login'); // Redirect to the login page if not authenticated
  } else {
    next();
  }
});

export default router;
