<template>
  <div class="bg-gray-100">
 <header class="bg-white shadow py-4 fixed w-full z-10">
      <nav class="container mx-auto px-4 flex items-center justify-between">
        <div>
          <a href="#" class="text-xl font-bold text-gray-800">Logo</a>
        </div>
        <div class="flex items-center space-x-4">
          <ul class="flex space-x-4">
            <li><a href="#" class="text-gray-600 hover:text-gray-800">Home</a></li>
            <li><a href="#" class="text-gray-600 hover:text-gray-800">About</a></li>
            <li><a href="#" class="text-gray-600 hover:text-gray-800">Blogs</a></li>
            <li><a href="#" class="text-gray-600 hover:text-gray-800">Services</a></li>
            <li><a href="#" class="text-gray-600 hover:text-gray-800">Contact</a></li>
          </ul>
          <a href="/login" class="ml-4 bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded">Login</a>
        </div>
      </nav>
    </header>

    <main>
      <section class="py-10">
        <div class="container mx-auto flex items-center justify-center">
          <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
            <div class="px-4 mt-[40%]">
              <h1 class="text-4xl font-bold mb-4">Welcome to Our Platform</h1>
              <p class="text-gray-600 mb-6">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam ut malesuada tortor.</p>
              <a href="#" class="inline-block bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded">Get Started</a>
            </div>
            <div class="px-4">
              <img src="../assets/image1.png" alt="Platform" class=" h-84 object-cover rounded-lg" />
            </div>
          </div>
        </div>
      </section>

      <section class="bg-white py-10">
        <div class="container mx-auto">
          <h2 class="text-3xl font-bold mb-6">Why Choose Our Platform?</h2>
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <div class="px-4">
              <h3 class="text-xl font-semibold mb-4">Feature 1</h3>
              <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam ut malesuada tortor.</p>
            </div>
            <div class="px-4">
              <h3 class="text-xl font-semibold mb-4">Feature 2</h3>
              <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam ut malesuada tortor.</p>
            </div>
            <div class="px-4">
              <h3 class="text-xl font-semibold mb-4">Feature 3</h3>
              <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam ut malesuada tortor.</p>
            </div>
          </div>
        </div>
      </section>

      <!-- Add more sections or content as needed -->

    </main>

    <footer class="bg-gray-800 text-white py-8">
        <div class="container mx-auto">
          <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div>
              <h3 class="text-xl font-bold mb-4">Company</h3>
              <ul class="space-y-2">
                <li><a href="#" class="text-gray-300 hover:text-white">About</a></li>
                <li><a href="#" class="text-gray-300 hover:text-white">Services</a></li>
                <li><a href="#" class="text-gray-300 hover:text-white">Contact</a></li>
                <li><a href="#" class="text-gray-300 hover:text-white">Terms of Service</a></li>
                <li><a href="#" class="text-gray-300 hover:text-white">Privacy Policy</a></li>
              </ul>
            </div>
            <div>
              <h3 class="text-xl font-bold mb-4">Resources</h3>
              <ul class="space-y-2">
                <li><a href="#" class="text-gray-300 hover:text-white">Blog</a></li>
                <li><a href="#" class="text-gray-300 hover:text-white">Whitepapers</a></li>
                <li><a href="#" class="text-gray-300 hover:text-white">Case Studies</a></li>
              </ul>
            </div>
            <div>
              <h3 class="text-xl font-bold mb-4">Connect</h3>
              <ul class="space-y-2">
                <li><a href="#" class="text-gray-300 hover:text-white">Twitter</a></li>
                <li><a href="#" class="text-gray-300 hover:text-white">LinkedIn</a></li>
                <li><a href="#" class="text-gray-300 hover:text-white">Facebook</a></li>
                <li><a href="#" class="text-gray-300 hover:text-white">Instagram</a></li>
              </ul>
            </div>
          </div>
          <div class="border-t border-gray-600 mt-8 pt-6">
            <p class="text-center text-gray-400">&copy; 2023 Your Company. All rights reserved.</p>
          </div>
        </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'LandingPage',
  // Add your component logic here
}
</script>

<style scoped>
/* Add your custom styles here */
</style>

