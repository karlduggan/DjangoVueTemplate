<template>
    <div class="flex h-screen bg-gray-200">
      <div class="w-1/5 bg-white">
        <!-- Sidebar content -->
        <nav class="px-4 py-6">
          <ul class="space-y-2">
            <li>
              <router-link to="/dashboard" class="text-blue-600 hover:text-blue-700">Dashboard</router-link>
            </li>
            <li>
              <router-link to="/projects" class="text-blue-600 hover:text-blue-700">Projects</router-link>
            </li>
            <li>
              <router-link to="/settings" class="text-blue-600 hover:text-blue-700">Settings</router-link>
            </li>
          </ul>
        </nav>
      </div>
      <div class="w-4/5 bg-gray-200">
        <!-- Main content -->
        <div class="px-4 py-6">
          <h1 class="text-2xl font-bold mb-4">Dashboard</h1>
          <p>Welcome to your dashboard!</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'DashboardPage',
  };
  </script>
  
  <style>
  </style>
  