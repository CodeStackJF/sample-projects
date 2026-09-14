<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;

class Clients extends Model
{
    use HasFactory;
    
    protected $fillable = [
        'first_name',
        'last_name',
        'email',
        'phone_number'
    ];

    public function phoneNumbers():HasMany
    {
        return $this->hasMany(PhoneNumbers::class, 'client_id', 'id');
    }
}