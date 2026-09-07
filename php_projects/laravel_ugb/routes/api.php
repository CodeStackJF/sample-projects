<?php

use App\Http\Controllers\ClientAPIController;
use Illuminate\Support\Facades\Route;

Route::get('/clients', [ClientAPIController::class, 'index']);
Route::post('/clients', [ClientAPIController::class, 'save']);
Route::get('/clients/{client}', [ClientAPIController::class, 'view']);
Route::put('/clients/{client}', [ClientAPIController::class, 'update']);
Route::patch('/clients/{client}', [ClientAPIController::class, 'update']);
Route::delete('/clients/{client}', [ClientAPIController::class, 'delete']);