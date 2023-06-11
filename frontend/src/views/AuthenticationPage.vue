<template>
  <div class="flex items-center justify-center min-h-screen bg-gray-100">
    <div class="max-w-md w-full">
      <h2 class="text-3xl font-bold text-center mb-4">Login</h2>
      <form class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4" @submit.prevent="login">
        <div class="text-left mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="username">Username</label>
          <input v-model="username" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="username" type="text" placeholder="Enter your username" required>
        </div>
        <div class="text-left mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="password">Password</label>
          <input v-model="password" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="password" type="password" placeholder="Enter your password" required>
        </div>
        <div>
          <button class="w-full bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="submit">Login</button>
        </div>
        <div>  
          <button class="w-full mt-5 bg-gray-900 hover:bg-gray-500 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" @click="createAccount">Create an Account</button>
        </div>
        <div>
          <a class="inline-block mt-5 align-baseline font-bold text-sm text-blue-500 hover:text-blue-800" href="#">Forgot Password?</a>
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

const API_URL = '/api/v1/login/';

export default {
  name: 'AuthenticationPage',
  data() {
    return {
      username: '',
      password: '',
      errorMessage: '',
    };
  },
  methods: {
    login() {
      this.errorMessage = '';

      axios.post(API_URL, {
        username: this.username,
        password: this.password,
      })
        .then(response => {
          // Handle successful login
          console.log(response.data.token);
          localStorage.setItem('token', response.data.token);
          this.$router.push('/dashboard');
          this.$store.commit('setLoggedIn', true);
        })
        .catch(error => {
          // Handle login error, such as displaying an error message
          console.error(error);
          if (error.response && error.response.status === 401) {
            // Incorrect username or password
            this.errorMessage = 'Incorrect username or password';
          } else {
            // Other error occurred
            this.errorMessage = 'An error occurred. Please try again later.';
          }
        });
    },
    createAccount() {
      this.$router.push('/create-account');
    },
  },
};
</script>

<style>
/* Add your custom styles here */
</style>
