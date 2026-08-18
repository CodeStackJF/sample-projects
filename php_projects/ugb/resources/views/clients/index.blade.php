<x-layout>
    <h1>Clients</h1>

    <x-slot:name>
        Pedro
    </x-slot:name>

    <div class="container">
        <form method="post" action="/clients">
            <div class="row">
                <div class="col-md-3 form-group">
                    <label>First name</label>
                    <input type="text" class="form-control" name="first_name" value="{{ old('first_name') }}">
                    @error('first_name')
                        <div class="label">
                            <span class="">{{$message}}</span>
                        </div>
                    @enderror
                </div>
                <div class="col-md-3 form-group">
                    <label>Last name</label>
                    <input type="text" class="form-control" name="last_name" value="{{ old('last_name') }}">
                    @error('last_name')
                        <div class="label">
                            <span class="">{{$message}}</span>
                        </div>
                    @enderror
                </div>
            </div>
            <div class="row">
                <div class="col-md-3 form-group">
                    <label>Email</label>
                    <input type="text" class="form-control" name="email" value="{{ old('email') }}">
                    @error('email')
                        <div class="label">
                            <span class="">{{$message}}</span>
                        </div>
                    @enderror
                </div>
                <div class="col-md-2 form-group">
                    <label>Phone Number</label>
                    <input type="text" class="form-control" name="phone_number" value="{{ old('phone_number') }}">
                    @error('phone_number')
                        <div class="label">
                            <span class="">{{$message}}</span>
                        </div>
                    @enderror
                </div>
            </div>
            <br>
            <div class="row">
                <div class="col-md-2 form-group"><button type="submit" class="btn btn-primary form-control">Add</button></div>
                <div class="col-md-2 form-group"><button type="reset" class="btn btn-warning form-control">Reset</button></div>
            </div>
        </form>
    </div>
    <br>
    <div class="row">
        @foreach ($clients as $client)
        <div class="card">
            <div class="card-header">
                {{ $client->first_name }} {{ $client->last_name }}
            </div>
            <div class="card-body">
                <h5 class="card-title">{{$client->email}}</h5>
                <p class="card-text">Phone Number: {{$client->phone_number}}</p>
                <ul>
                    @foreach($client->phoneNumbers as $phone_number)
                        <li>({{$phone_number->area_code}}) {{$phone_number->phone}}</li>
                    @endforeach
                </ul>
                <small>Created at: {{$client->created_at}} | Updated at: {{$client->updated_at}}</small>
                <hr>
                <a href="/clients/{{ $client->id }}/view" class="btn btn-primary">View</a>
                <a href="/clients/{{ $client->id }}/edit" class="btn btn-primary">Edit</a>
                <a href="/clients/{{ $client->id }}/delete" class="btn btn-primary">Delete</a>
            </div>
            </div>
        @endforeach
    </div>
</x-layout>