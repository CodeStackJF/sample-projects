<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Clients extends Model
{
    protected $fillable = [
        'first_name',
        'last_name',
        'email',
        'phone_number'
    ];
}
