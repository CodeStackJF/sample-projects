<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Client;
use Illuminate\Support\Facades\DB;
use Illuminate\Database\Query\Builder;
use Illuminate\Validation\ValidationException;
use Illuminate\Validation\Rule;

class ClientController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        $clients = Client::get();
        return view('/clients/index', ['clients' => $clients]);
    }

    public function view(Client $client)
    {
        return view('/clients/view', ['client' => $client]);
    }

    public function edit(Client $client)
    {
        return view('/clients/edit', compact('client'));
    }

    public function create(Request $request)
    {
        $validated = $request->validate([
            "first_name" => 'required|string|max:30|min:5',
            "last_name" => 'required|string|max:30|min:5',
            'email' => 'required|unique:clients',
            'document' => 'required|unique:clients'
        ],
        [
            'first_name.required' => 'Write first name',
            'first_name.max' => 'only 30 chars allowed',
            'first_name.min' => 'write at least 4 chars',
            'last_name.required' => 'Write first name',
            'last_name.max' => 'only 30 chars allowed',
            'last_name.min' => 'write at least 4 chars',
            'email.unique' => 'Email is already registered',
        ]);

        
        $client = Client::create([
            'first_name' => $validated['first_name'],
            'last_name' => $validated['last_name'],
            'email' => $validated['email'],
            'document' => $validated['document']
        ]);
        return redirect('/clients')->with('success', 'Client created successfully');
    }

    public function update(Request $request, Client $client)
    {
        $validated = $request->validate([
            "first_name" => 'required|string|max:30|min:5',
            "last_name" => 'required|string|max:30|min:5',
            'email' =>  [
                'required',
                'email',
                Rule::unique('clients', 'email')->ignore($client->id)
            ],
            'document' =>  [
                'required',
                Rule::unique('clients', 'document')->ignore($client->id)
            ]
        ],
        [
            'first_name.required' => 'Write first name',
            'first_name.max' => 'only 30 chars allowed',
            'first_name.min' => 'write at least 4 chars',
            'last_name.required' => 'Write last name',
            'last_name.max' => 'only 30 chars allowed',
            'last_name.min' => 'write at least 4 chars',
            'email.required' => 'Email is required.',
            'email.email' => 'Invalid email format.',
            'email.unique' => 'This email is already registered to another client.',

            'document.required' => 'Document is required.',
            'document.unique' => 'This document is already registered to another client.',
        ]);

        $email_exists = Client::where('clients.email', $validated['email'])->whereNot('clients.id', $client->id)->exists();

        if($email_exists)
        {
            throw ValidationException::withMessages([
                'email' => 'This email is used by another client'
            ]);
        }

         $document_exists = Client::where('clients.document', $validated['document'])->whereNot('clients.id', $client->id)->exists();

        if($document_exists)
        {
            throw ValidationException::withMessages([
                'document' => 'Document is already used by another client'
            ]);
        }

        $client = $client->update([
            'first_name' => $validated['first_name'],
            'last_name' => $validated['last_name'],
            'email' => $validated['email'],
            'document' => $validated['document']
        ]);
        return redirect('/clients')->with('success', 'Client updated successfully');
    }

    public function delete(Client $client)
    {
        $client->delete();
        return redirect('/clients')->with('success', 'Client deleted');
    }
}
