<x-layout>
    <form method="post" action="/clients/{{ $client->id }}/update">
            <div class="row">
                <div class="col-md-3 form-group">
                    <label>First name</label>
                    <input type="text" class="form-control" name="first_name" value="{{ $client->first_name }}">
                    @error('first_name')
                        <div class="label">
                            <span class="">{{$message}}</span>
                        </div>
                    @enderror
                </div>
                <div class="col-md-3 form-group">
                    <label>Last name</label>
                    <input type="text" class="form-control" name="last_name" value="{{ $client->last_name }}">
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
                    <input type="text" class="form-control" name="email" value="{{ $client->email }}">
                    @error('email')
                        <div class="label">
                            <span class="">{{$message}}</span>
                        </div>
                    @enderror
                </div>
                <div class="col-md-2 form-group">
                    <label>Phone Number</label>
                    <input type="text" class="form-control" name="phone_number" value="{{ $client->phone_number }}">
                    @error('phone_number')
                        <div class="label">
                            <span class="">{{$message}}</span>
                        </div>
                    @enderror
                </div>
            </div>
            <br>
            <div class="row">
                <div class="col-md-2 form-group"><button type="submit" class="btn btn-primary form-control">Update</button></div>
                <div class="col-md-2 form-group"><a href="/clients" type="reset" class="btn btn-warning form-control">Return</a></div>
            </div>
        </form>
</x-layout>