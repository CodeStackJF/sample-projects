<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class Addresses extends Model
{
    protected $fillable = [
        'client_id',
        'street',
        'avenue'
    ];

    public function user():BelongsTo
    {
        return $this->belongsTo(User::class, 'client_id');
    }
}
