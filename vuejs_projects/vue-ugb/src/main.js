import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap'
import axios from 'axios'
import VueAxios from 'vue-axios'

axios.defaults.baseURL = import.meta.env.VITE_APP_ENV_VARIABLE

var token = localStorage.getItem('token');
if(token)
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + localStorage.getItem('token');

axios.interceptors.response.use(function (response) {
    return response
    }, function (error) {
    if (error.response.status === 401) {
        router.push('/')
    }
    if(error.response.status === 403)
    {
        router.push('/');
    }
    if(error.response.status === 500)
    {
        console.log('Ha ocurrido un error de conexión al servidor.');
    }
    return Promise.reject(error)
})

const app = createApp(App)

app.use(router).use(VueAxios, axios)

app.mount('#app')
