<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class PhoneNumbers extends Model
{
    protected $table = 'phone_numbers';

    protected $fillable = [
        'phone',
        'area_code',
        'client_id'
    ];

    public function client()
    {
        return $this->belongsTo(Clients::class, 'client_id', 'id');
    }
}
