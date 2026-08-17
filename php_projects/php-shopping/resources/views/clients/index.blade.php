<x-layout>
    <div class="row">
        <div class="col-md-12">
            <form method="post" action="/clients/create">
                @if(session('success'))
                    <div class="alert alert-success">
                        {{ session('success') }}
                    </div>
                @endif
                <div class="row">
                    <div class="col-md-3 form-group">
                        <label>First Name</label>
                        <input type="text" name="first_name" class="form-control" maxlength="30">
                        @error('first_name')
                            <div class="label">
                                <span class="">{{$message}}</span>
                            </div>
                        @enderror
                    </div>
                     <div class="col-md-3 form-group">
                        <label>Last Name</label>
                        <input type="text" name="last_name" class="form-control" maxlength="30">
                        @error('last_name')
                            <div class="label">
                                <span class="">{{$message}}</span>
                            </div>
                        @enderror
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-3">
                        <label>Email</label>
                        <input type="text" name="email" class="form-control" maxlength="200">
                        @error('email')
                            <div class="label">
                                <span class="">{{$message}}</span>
                            </div>
                        @enderror
                    </div>
                    <div class="col-md-3">
                        <label>Document</label>
                        <input type="text" name="document" class="form-control" maxlength="10">
                        @error('document')
                            <div class="label">
                                <span class="">{{$message}}</span>
                            </div>
                        @enderror
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-12">
                        <button type="submit" class="btn btn-primary">Guardar</button>
                        <button type="reset" class="btn btn-warning">Cancelar</button>
                    </div>
                </div>
            </form>
        </div>
    </div>

    <div class="row">
        <div class="col-md-12">
            <table class="table table-condensed table-bordered">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>First Name</th>
                        <th>Last Name</th>
                        <th>Email</th>
                        <th>Document</th>
                        <th></th>
                        <th></th>
                        <th></th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    @foreach($clients as $client)
                        <tr>
                            <td>{{$client->id}}</td>
                            <td>{{$client->first_name}}</td>
                            <td>{{$client->last_name}}</td>
                            <td>{{$client->email}}</td>
                            <td>{{$client->document}}</td>
                            <td><a href="/clients/{{$client->id}}/view">View</a></td>
                            <td><a href="/clients/{{$client->id}}/edit">Edit</a></td>
                            <td><a href="/clients/{{$client->id}}/delete">Delete</a></td>
                            <td><a href="/clients/{{$client->id}}/addresses">Add</a></td>
                        </tr>
                    @endforeach
                </tbody>
            </table>
        </div>
    </div>
</x-layout>