<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Ambiente extends Model
{
    protected $table = 'ambientes';

    protected $fillable = [
        'nome',
        'capacidade',
        'tipo',
    ];

    public function ofertas()
    {
        return $this->hasMany(Oferta::class);
    }
}
