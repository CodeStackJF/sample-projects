<x-layout>
    <div class="row">
        <div class="col-md-3 form-group">
            <label>First name</label>
            <p>{{ $client->first_name }}</p>
        </div>
        <div class="col-md-3 form-group">
            <label>Last name</label>
            <p>{{ $client->last_name }}</p>
        </div>
    </div>
    <div class="row">
        <div class="col-md-3 form-group">
            <label>Email</label>
            <p>{{ $client->email }}</p>
        </div>
        <div class="col-md-2 form-group">
            <label>Phone Number</label>
            <p>{{ $client->phone_number }}</p>
        </div>
    </div>
    <br>
    <div class="row">
        <div class="col-md-2 form-group"><a href="/clients" type="reset" class="btn btn-warning form-control">Return</a></div>
    </div>
</x-layout>