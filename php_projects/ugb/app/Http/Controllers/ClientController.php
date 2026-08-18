<?php

namespace App\Http\Controllers;

use App\Models\Clients;
use Illuminate\Http\Request;
use Illuminate\Validation\Rule;

class ClientController extends Controller
{
    public function index()
    {
        $clients = Clients::get();
        return view('clients.index', ['clients' => $clients]);
    }

    public function save(Request $request)
    {
        $validated = $request->validate([
            "first_name" => 'required|string|max:30|min:5',
            "last_name" => 'required|string|max:30|min:5',
            'phone_number' => 'required',
            'email' => 'required|unique:clients'
        ],
        [
            'first_name.required' => 'Write first name',
            'first_name.max' => 'only 30 chars allowed',
            'first_name.min' => 'write at least 4 chars',
            'last_name.required' => 'Write last name',
            'last_name.max' => 'only 30 chars allowed',
            'last_name.min' => 'write at least 4 chars',
            'email.unique' => 'Email is already registered',
        ]);

        
        $client = Clients::create([
            'first_name' => $validated['first_name'],
            'last_name' => $validated['last_name'],
            'email' => $validated['email'],
            'phone_number' => $validated['phone_number']
        ]);
        return redirect('/clients')->with('success', 'Client created successfully');
    }

    public function delete(Clients $client)
    {
        if(Clients::find($client->id))
        {
            $client->delete();
            return redirect('/clients')->with('success', 'Client has been deleted.');
        }
        else
        {
            abort(404, 'The requested item was not found.');
        }
        
    }

    public function view(Clients $client)
    {
        if(Clients::find($client->id))
        {
            return view('clients.view', ['client' => $client]);
        }
        else
        {
            abort(404, 'The requested item was not found.');
        }        
    }

    public function edit(Clients $client)
    {
        if(Clients::find($client->id))
        {
            return view('clients.edit', ['client' => $client] );
        }
        else
        {
            abort(404, 'The requested item was not found.');
        }        
    }

    public function update(Request $request, Clients $client)
    {
        $validated = $request->validate([
            "first_name" => 'required|string|max:30|min:5',
            "last_name" => 'required|string|max:30|min:5',
            'phone_number' => 'required',
            'email' => [
                'required',
                'email',
                Rule::unique('clients', 'email')->ignore($client->id)
            ]
        ],
        [
            'first_name.required' => 'Write first name',
            'first_name.max' => 'only 30 chars allowed',
            'first_name.min' => 'write at least 4 chars',
            'last_name.required' => 'Write last name',
            'last_name.max' => 'only 30 chars allowed',
            'last_name.min' => 'write at least 4 chars',
            'email.unique' => 'Email is already registered',
        ]);

        
        $client->update([
            'first_name' => $validated['first_name'],
            'last_name' => $validated['last_name'],
            'email' => $validated['email'],
            'phone_number' => $validated['phone_number']
        ]);
        return redirect('/clients')->with('success', 'Client created successfully');
    }
}