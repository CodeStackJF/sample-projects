<template>
    <!-- <h1>Clients</h1>
    <label>{{name}}</label>

    <input type="text" v-model="name">

    {{fruta}}
    <select class="form-control" v-model="fruta">
        <option value=0>Seleccione</option>
        <option value=1>Manzana</option>
        <option value=2>pera</option>
        <option value=3>Uva</option>
        <option value=4>melocotón</option>
    </select> -->

    <div>
        <!-- <button type="button" class="btn btn-primary" v-on:click="getClients()">Get Clients</button>
        <button type="button" class="btn btn-primary" @click="getClients()">Get Clients</button> -->

        <div class="row">
            <div class="col-md-12">
                <form id="frm-clients" @submit.prevent="saveClient()">
                    <div class="row">
                        <div class="col-md-2 form-group">
                            <label>First name</label>
                            <input type="text" v-model="client.first_name" id="txt_first_name">
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-md-2 form-group">
                            <button type="submit" class="btn btn-primary">Save</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
       <div class="row">
            <div class="col-md-12">
                <table class="table table-bordered">
                    <thead>
                        <tr>
                        <th>ID</th>
                        <th>First name</th>
                        <th>Last name</th>
                        <th>Email</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="client in clients">
                            <td>{{client.id}}</td>
                            <td>{{client.first_name}}</td>
                            <td>{{client.last_name}}</td>
                            <td>{{client.email}}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
       </div>
    </div>
</template>

<script>
export default {
    data(){
        return {
            name: 'jose',
            fruta: 0,
            clients: [],
            client: {
               
            },
            apiCall: {},

            /*first_name: '',
            last_name: '',
            email: ''*/
        }
    },
    async mounted()
    {
        await this.getClients();
    },
    created(){
        //se ejecuta en el momento de llamar el componente
        //pero hasta ese momento no ha renderizado ningun elemento html
    },
    methods: {
        sumar(a, b)
        {
            return a + b;
        },
        async getClients()
        {
            console.log("La carga ha comenzado")
            await this.axios.get('http://localhost:5131/clients')
            .then(response => {
                //console.log(response.data);
                this.clients = response.data;
            });
            console.log("La carga ha finalizado")
        },
        async saveClient()
        {
            console.log(this.client);
            let first_name = document.querySelector('#txt_first_name').value;
            console.log(first_name);
        }
    }
}
</script>