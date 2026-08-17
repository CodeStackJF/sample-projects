<x-layout>
    <h1>Clients</h1>

    <x-slot:name>
        Pedro
    </x-slot:name>
    @foreach ($clients as $client)
    <div class="card">
        <div class="card-header">
            {{ $client->first_name }} {{ $client->last_name }}
        </div>
        <div class="card-body">
            <h5 class="card-title">{{$client->email}}</h5>
            <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
            <a href="#" class="btn btn-primary">Go somewhere</a>
        </div>
        </div>
@endforeach
</x-layout>