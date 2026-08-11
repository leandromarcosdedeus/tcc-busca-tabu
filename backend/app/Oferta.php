<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Oferta extends Model
{
    protected $table = 'ofertas';

    protected $fillable = [
        'curso_id',
        'disciplina',
        'turma',
        'professor_id',
        'carga_horaria',
        'horario_id',
        'ambiente_id',
    ];

    public function curso()
    {
        return $this->belongsTo(Curso::class);
    }

    public function professor()
    {
        return $this->belongsTo(Professor::class);
    }

    public function horario()
    {
        return $this->belongsTo(Horario::class);
    }

    public function ambiente()
    {
        return $this->belongsTo(Ambiente::class);
    }
}
