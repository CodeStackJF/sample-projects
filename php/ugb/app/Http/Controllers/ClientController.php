<?php

namespace App\Http\Controllers;

use App\Models\Clients;
use Illuminate\Http\Request;

class ClientController extends Controller
{
    public function index()
    {
        $clients = Clients::get();
        return view('clients.index', ['clients' => $clients]);
    }
}
