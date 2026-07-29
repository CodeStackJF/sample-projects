<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\ClientController;
use App\Http\Controllers\AddressesController;
use App\Models\Client;

Route::get('/', function () {
    return view('welcome');
});


Route::get('/clients', [ClientController::class, 'index']);
Route::get('/clients/{client}/view', [ClientController::class, 'view']);
Route::get('/clients/{client}/edit', [ClientController::class, 'edit']);
Route::post('/clients/{client}/update', [ClientController::class, 'update']);
Route::get('/clients/{client}/delete', [ClientController::class, 'delete']);
Route::post('/clients/create', [ClientController::class, 'create']);

Route::get('/clients/{client}/addresses', [AddressesController::class, 'index']);