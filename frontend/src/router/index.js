// src/router/index.js

import { createRouter, createWebHistory } from 'vue-router';
import LandingPage from "../views/LandingPage"

const routes = [
  {
    path: '/',
    name: 'Home',
    component: LandingPage,
  },
 
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;