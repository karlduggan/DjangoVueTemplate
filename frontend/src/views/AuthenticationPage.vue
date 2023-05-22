<template>
    <div class="flex items-center justify-center min-h-screen bg-gray-100">
      <div class="max-w-md w-full">
        <h2 class="text-3xl font-bold text-center mb-4">Login</h2>
        <form class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
          <div class="text-left mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="username">Username</label>
            <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="username" type="text" placeholder="Enter your username">
          </div>
          <div class="text-left mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="password">Password</label>
            <input class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="password" type="password" placeholder="Enter your password">
          </div>
          <div class="flex items-center justify-between">
            <button class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="button">Login</button>
            <a class="inline-block align-baseline font-bold text-sm text-blue-500 hover:text-blue-800" href="#">Forgot Password?</a>
          </div>
        </form>
        <p class="text-center text-gray-500 text-xs">
          &copy; 2023 Your Company. All rights reserved.
        </p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'AuthenticationPage',
    // Add your component logic here
  }
  </script>
  
  <style scoped>
  /* Add your custom styles here */
  </style>
  