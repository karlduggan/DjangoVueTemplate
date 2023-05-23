// src/router/index.js

import { createRouter, createWebHistory } from 'vue-router';
import LandingPage from "../views/LandingPage"
import AuthenticationPage from "../views/AuthenticationPage"
import DashboardPage from "../views/DashboardPage"
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
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;