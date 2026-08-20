<template>
    <div class="row">
        <div class="col-md-12">
            <table class="table table-dark">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>First Name</th>
                        <th>Last Name</th>
                        <th>Email</th>
                        <th>View</th>
                        <th>Edit</th>
                        <th>Delete</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="pokemon in pokemons" :key="pokemon.name">
                        <td>{{ pokemon.name }}</td>
                        <td>{{ pokemon.url }}</td>
                        <td><a href="#!" class="btn btn-primary">View</a></td>
                        <td><a href="#!" class="btn btn-warning">Edit</a></td>
                        <td><a href="#!" class="btn btn-danger">Delete</a></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
    export default {
        data()
        {
            return {
                name: 'jose',
                pokemons: []
            }
        },
        async mounted()
        {
            await this.getPokemons();
            await this.login();
        },
        methods: {
            async getPokemons()
            {
                await this.axios.get('/pokemon')
                .then(response => {
                    this.pokemons= response.data.results;
                });
            },
            async login()
            {
                let token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1laWQiOiJqb3NlX2NhbXBvcyIsIlJlZ2lvbmFsIjoiMSIsIkNpY2xvIjoiNDQ2IiwiQ29kaWdvIjoiMTc3NSIsIkFuaW8iOiIyMDI2IiwiQ29kY2ljIjoiMyIsIkNvZE1hdVByZWdyYWRvIjoiNjAwIiwiQ29kTWF1UG9zZ3JhZG8iOiIwIiwiQWRtaW5pc3RyYWRvciI6IlMiLCJyb2xlIjpbIkhvcmFyaW9zIiwiVmlydHVhbCIsIkZlY2hhc1ZpcnR1YWxlcyIsIlByb3llY2Npb24iLCJNYXRlcmlhc1Byb2dyYW1hZGFzIiwiQ3J1emFkYXMiLCJTaW5Ib3JhcmlvcyIsIlNpbkRvY2VudGUiLCJGZWNoYXMiLCJHZW5lcmFjaW9uIiwiR3J1cG9zIiwiQWRtaW5pc3RyYWNpb24iLCJSZXN0cmljY2lvbmVzIiwiQWNjZXNvc1VPbmxpbmUiLCJHZXN0aW9uIiwiUHJvY2Vzb3NHcmFkdWFjaW9uIiwiR2VuZXJhY2lvbiIsIkNvbmZpZ3VyYWNpb24iLCJEb2NlbnRlcyIsIkZlY2hhc05vdGFzVmlydHVhbGVzIiwiUHJvZ3JhbWFjaW9uVmlydHVhbGVzIiwiQXVsYXNNYXRlcmlhIiwiQmxvcXVlc1JlZ2lvbmFsIiwiQXV0b3JpemFjaW9uIiwiTW92aW1pZW50b3MiLCJQcm9jZXNvR3JhZHVhY2lvbiIsIkFkbWluaXN0cmFkb3IiLCJBY2FkZW1pY2EiXSwibmJmIjoxNzg3MjU3MTI0LCJleHAiOjE3ODczMzk5MjQsImlhdCI6MTc4NzI1NzEyNH0.qOSPJgLnx2VtIElYeFQRV5Hivfaaxn_84568czBAEsk";
                 this.axios.defaults.headers.common['Authorization'] = 'Bearer ' + token;                    
                    localStorage.setItem('token', token);
                    this.$store.commit('setAuthenticated', true);
                    this.$store.commit('setUserData', "userData");
                    this.$store.commit('setMenus', "setMenus");
                    this.$router.push('/');
            }
        }
    }
</script>