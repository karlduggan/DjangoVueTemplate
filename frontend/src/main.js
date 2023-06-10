import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index'
import store from './store/index'
import './styles/styles.css'
import axios from 'axios'
import './styles/index.css'

// Setup to the backend "Django"
axios.defaults.baseURL = "http://127.0.0.1:8000"

const app = createApp(App)

app.use(router)
app.use(store)

app.mount('#app')