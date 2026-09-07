<x-layout>
<h1>Users</h1>

@foreach ($users as $user)
    <div class="card">
        <div class="card-header">
            {{ $user['name'] }}
        </div>
        <div class="card-body">
            <h5 class="card-title">{{$user['email']}}</h5>
            <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
            <a href="#" class="btn btn-primary">Go somewhere</a>
        </div>
        </div>
@endforeach
</x-layout>
