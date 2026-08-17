<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;

class Client extends Model
{
    protected $fillable = [
        'first_name',
        'last_name',
        'email', // Add your field here
        'document', // Add your field here
    ];

    public function addresses():HasMany
    {
        return $this->hasMany(Addresses::class);
    }
}
