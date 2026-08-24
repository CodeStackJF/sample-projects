<template>
    <div>{{ clients }}</div>
</template>

<script>
export default {
    data(){
        return {
            URL_BASE: '',
            clients: []
        }
    },
    async mounted(){
        this.URL_BASE = import.meta.env.VITE_URL_BASE_LARAVEL;
        await this.getClients();
    },
    methods:{
        async getClients()
        {
            await this.axios.get(this.URL_BASE + 'api/clients')
            .then(response => {
                this.clients = response.data;
            })
        }
    }
}
</script>