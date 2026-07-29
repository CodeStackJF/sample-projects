<x-layout>
<div class="row">
        <div class="col-md-12">
            <form method="post" action="/clients/{{ $client->id }}/update">
                @method('POST')
                @if(session('success'))
                    <div class="alert alert-success">
                        {{ session('success') }}
                    </div>
                @endif
                <div class="row">
                    <div class="col-md-3 form-group">
                        <label>First Name</label>
                        <input type="text" name="first_name" class="form-control" value="{{ old('first_name', $client->first_name) }}" maxlength="30">
                        @error('first_name')
                            <div class="label">
                                <span class="">{{$message}}</span>
                            </div>
                        @enderror
                    </div>
                     <div class="col-md-3 form-group">
                        <label>Last Name</label>
                        <input type="text" name="last_name" class="form-control" value="{{ old('last_name', $client->last_name) }}" maxlength="30">
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
                        <input type="text" name="email" class="form-control" maxlength="200" value="{{ old('email', $client->email) }}">
                        @error('email')
                            <div class="label">
                                <span class="">{{$message}}</span>
                            </div>
                        @enderror
                    </div>
                    <div class="col-md-3">
                        <label>Document</label>
                        <input type="text" name="document" class="form-control" maxlength="10" value="{{ old('email', $client->document) }}">
                        @error('document')
                            <div class="label">
                                <span class="">{{$message}}</span>
                            </div>
                        @enderror
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-12">
                        <button type="submit" class="btn btn-primary">Update</button>
                        <a href="/clients" class="card-link btn btn-warning">Back</a>
                    </div>
                </div>
            </form>
        </div>
    </div>
</x-layout>