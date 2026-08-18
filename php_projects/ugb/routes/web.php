<?php

use App\Http\Controllers\ClientController;
use App\Http\Controllers\UserController;
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

//get, delete, post, put, patch
Route::get('/about', function(){
    return view('about.index');
});

Route::get('/users', [UserController::class, 'index']);
Route::get('/clients', [ClientController::class, 'index']);
Route::post('/clients', [ClientController::class, 'save']);
Route::get('/clients/{client}/delete', [ClientController::class, 'delete']);
Route::get('/clients/{client}/edit', [ClientController::class, 'edit']);
Route::get('/clients/{client}/view', [ClientController::class, 'view']);
Route::post('/clients/{client}/update', [ClientController::class, 'update']);