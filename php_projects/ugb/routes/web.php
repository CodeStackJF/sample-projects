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