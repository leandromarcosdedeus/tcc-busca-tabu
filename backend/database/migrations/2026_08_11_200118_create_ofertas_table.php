<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateOfertasTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('ofertas', function (Blueprint $table) {
            $table->id();

            $table->foreignId('curso_id')
                ->constrained('cursos');

            $table->string('disciplina');
            $table->string('turma');

            $table->foreignId('professor_id')
                ->nullable()
                ->constrained('professores')
                ->nullOnDelete();

            $table->unsignedInteger('carga_horaria');

            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('ofertas');
    }
}
