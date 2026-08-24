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
        <button type="button" v-on:click="show = !show">{{show ? 'Ocultar':'Mostrar' }} Imagen</button>
        <br>
        <img src="https://ugb.edu.sv/wp-content/uploads/2025/10/UGB_LOGOTIPO_HORIZONTAL_POS-2.png.webp" v-show="show" height="200">
        <!--style="display:inline|none"-->
        <hr>
        <div class="row">
            <div class="col-md-12">
                <form id="frm-clients" @submit.prevent="client.id === 0 ? saveClient():updateClient()">
                    <div class="row">
                        <div class="col-md-3 form-group">
                            <label>ID</label>
                            <input type="text" v-model="client.id" disabled id="txt_id" class="form-control">
                        </div>
                        <div class="col-md-3 form-group">
                            <label>First name</label>
                            <input type="text" v-model="client.first_name" id="txt_first_name" class="form-control">
                            <ul v-show="validationErrors['first_name'] != undefined">
                                <li v-for="error in validationErrors['first_name']">{{error}}</li>
                            </ul>
                        </div>
                        <div class="col-md-3 form-group">
                            <label>Last name</label>
                            <input type="text" v-model="client.last_name" id="txt_last_name" class="form-control">
                            <ul v-show="validationErrors['last_name'] != undefined">
                                <li v-for="error in validationErrors['last_name']">{{error}}</li>
                            </ul>
                        </div>
                        <div class="col-md-3 form-group">
                            <label>Email</label>
                            <input type="email" v-model="client.email" id="txt_email" class="form-control">
                            <ul v-show="validationErrors['email'] != undefined">
                                <li v-for="error in validationErrors['email']">{{error}}</li>
                            </ul>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-md-2 form-group">
                            <button type="submit" class="btn btn-primary" v-bind:disabled="savingClient" v-if="client.id === 0">Save</button>
                            <button type="submit" class="btn btn-primary" v-bind:disabled="savingClient" v-if="client.id !== 0">Update</button>
                            <button type="reset" class="btn btn-warning" v-on:click="resetClientData()">Cancel</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
       <div class="row">
            <div class="col-md-12">
                <div class="spinner-border" role="status" v-show="loadingClients">
               
                </div>
                <table class="table table-bordered" v-show="!loadingClients">
                    <thead>
                        <tr>
                        <th>ID</th>
                        <th>First name</th>
                        <th>Last name</th>
                        <th>Email</th>
                        <th>Edit</th>
                        <th>Delete</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="client in clients">
                            <td>{{client.id}}</td>
                            <td>{{client.first_name}}</td>
                            <td>{{client.last_name}}</td>
                            <td>{{client.email}}</td>
                            <td><a href="#!" v-on:click="editClient(client.id)">Edit</a></td>
                            <td><a href="#!" v-on:click="deleteClient(client.id)">Delete</a></td>
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
            show: false,
            loadingClients: true,
            client: {
               id: 0
            },
            apiCall: {},

            validationErrors: [],
            showButton: false,
            savingClient: false
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
            await this.axios.get('/clients')
            .then(response => {
                this.clients = response.data;
                this.loadingClients = false;
            });
            console.log("La carga ha finalizado")
        },
        async saveClient()
        {
            this.validationErrors = [];
            this.savingClient = true;
            await this.axios.post('/clients', this.client)
            .then(async response => {
                this.clients.push(response.data);
                this.resetClientData();
            })
            .catch(error => {
                //4xx, 5xx
                
                if(error.response.status === 400)
                {
                    this.validationErrors = error.response.data.errors;
                    console.log(this.validationErrors);
                }

                if(error.response.status === 409)
                {
                    alert(error.response.data.message);
                }
            })
            .finally(() => {
                this.savingClient = false;
            });
        },
        async deleteClient(idClient){
            if(!confirm('Are you sure you want to delete this client?'))
            {
                return;
            }
            await this.axios.delete('/clients/' + idClient)
            .then(() =>{
                var index_client = this.clients.findIndex(x=>x.id == idClient);
                this.clients.splice(index_client, 1);
            })
            .catch(error => {
                if(error.response.status === 404)
                {
                    alert('Client not found');
                }
            });
        },
        async editClient(idClient){
            this.validationErrors = [];
            await this.axios.get('/clients/' + idClient)
            .then(response => {
                this.client = response.data;
            });
        },
        resetClientData(){
            this.client = {
                id: 0
            };
            this.validationErrors = [];
        },
        async updateClient()
        {
            await this.axios.put('/clients/' + this.client.id, this.client)
            .then(response => {
                 var index_client = this.clients.findIndex(x=>x.id == this.client.id);
                 this.clients[index_client] = response.data;
                 this.resetClientData();
            })
            .catch(error => {
                if(error.response.status === 400)
                {
                    this.validationErrors = error.response.data.errors;
                }

                if(error.response.status === 409)
                {
                    alert(error.response.data.message);
                }
            })
            .finally(() => {
                this.savingClient = false;
            });;
        }
    }
}
</script>