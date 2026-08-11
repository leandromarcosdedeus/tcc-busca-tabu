<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Curso extends Model
{
    protected $table = 'cursos';

    protected $fillable = [
        'nome',
        'codigo',
    ];

    public function ofertas()
    {
        return $this->hasMany(Oferta::class);
    }
}
