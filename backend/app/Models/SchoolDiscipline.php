<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class SchoolDiscipline extends Model
{
    use HasFactory;

    protected $fillable = [
        'discipline_code',
        'ch',
        'description',
    ];
}
