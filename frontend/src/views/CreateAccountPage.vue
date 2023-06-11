<template>
  <div class="flex items-center justify-center min-h-screen bg-gray-100">
    <div class="max-w-md w-full">
      <h2 class="text-3xl font-bold text-center mb-4">Create Account</h2>
      <form class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4" @submit.prevent="createAccount">
        <div class="text-left mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="username">Username</label>
          <input v-model="username" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="name" type="text" placeholder="Enter a username" required>
        </div>
        <div class="text-left mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="email">Email</label>
          <input v-model="email" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="email" type="email" placeholder="Enter your email" required>
        </div>
        <div class="text-left mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="password">Password</label>
          <input v-model="password" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="password" type="password" placeholder="Enter your password" required>
        </div>
        <div class="flex items-center justify-between">
          <button class="w-full mt-5 bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="submit">Create Account</button>
        </div>
        <!-- Add error message display -->
        <div v-if="errorMessage" class="text-red-500 text-center mt-4">{{ errorMessage }}</div>
      </form>
      <p class="text-center text-gray-500 text-xs">
        &copy; 2023 Your Company. All rights reserved.
      </p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

const API_URL = '/api/v1/create-account/';

export default {
  name: 'AccountCreationPage',
  data() {
    return {
      username: '',
      email: '',
      password: '',
      errorMessage: '',
    };
  },
  methods: {
    createAccount() {
      this.errorMessage = '';

      axios.post(API_URL, {
        username: this.username,
        email: this.email,
        password: this.password,
      })
        .then(response => {
          // Handle successful account creation
          console.log(response.data);
          this.$router.push('/login');
        })
        .catch(error => {
          // Handle account creation error, such as displaying an error message
          console.error(error);
          if (error.response && error.response.status === 409) {
            // Username or email already in use
            this.errorMessage = 'Username or email already exists';
          } else {
            // Other error occurred
            this.errorMessage = 'Error creating account, Username or email may already exists';
          }
        });
    },
  },
};
</script>

<style>
/* Add your custom styles here */
</style>
