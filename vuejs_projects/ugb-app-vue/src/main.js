import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'

axios.defaults.baseURL = import.meta.env.VITE_URL_BASE;

const app = createApp(App)

app.use(router).use(VueAxios, axios)

app.mount('#app')