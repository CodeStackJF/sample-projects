<x-layout>
    <div class="row">
        <div class="card">
            <div class="card-body">
                <div class="card-title"><b>Name: </b>{{$client->first_name}} {{$client->last_name}}</div>
                <div class="card-text">
                    <div class="row">
                        <div class="col-md-3">
                            <b>Email</b>
                            <p>
                                {{ $client->email }}
                            </p>
                        </div>
                        <div class="col-md-3">
                            <b>Document</b>
                            <p>
                                {{ $client->document }}
                            </p>
                        </div>
                    </div>
                    <a href="/clients" class="card-link btn btn-primary">Back</a>
                </div>
            </div>
        </div>
    </div>
    <div>
        {{ json_encode($addresses) }}
    </div>
</x-layout>