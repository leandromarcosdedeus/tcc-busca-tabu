<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Disciplina;
use App\Models\Professor;
use App\Models\Turma;
use App\Models\Alocacao;
//use Illuminate\Http\Request;
use Maatwebsite\Excel\Facades\Excel;
use Illuminate\Support\Facades\DB;


class PlannerController extends Controller
{
    public function importar(Request $request)
    {
        $request->validate([
            'arquivo' => 'required|file|mimes:xlsx,xls'
        ]);

        $file = $request->file('arquivo');

        $dados = Excel::toCollection(null, $file)[0]; // Aba 0 = Disciplinas oferta 2024

        DB::beginTransaction();

        try {
            foreach ($dados->skip(1) as $linha) { // pula cabeçalho
                if (empty($linha[2])) continue; // ignora linhas vazias

                // Turma
                $turma = Turma::firstOrCreate([
                    'ano' => $linha[0],
                    'serie' => $linha[1],
                ]);

                // Disciplina
                $disciplina = Disciplina::firstOrCreate([
                    'codigo' => $linha[2],
                ], [
                    'nome' => $linha[3],
                    'carga_horaria' => $linha[4],
                ]);

                // Professor titular
                $professor = null;
                if (!empty($linha[6])) {
                    $professor = Professor::firstOrCreate(['nome' => $linha[6]]);
                }

                // Professor backup
                $backup = null;
                if (!empty($linha[7])) {
                    $backup = Professor::firstOrCreate(['nome' => $linha[7]]);
                }

                // Alocação
                Alocacao::create([
                    'disciplina_id' => $disciplina->id,
                    'turma_id' => $turma->id,
                    'professor_id' => optional($professor)->id,
                    'professor_backup_id' => optional($backup)->id,
                    'ambiente' => $linha[8] ?? null,
                ]);
            }

            DB::commit();

            return response()->json(['status' => 'sucesso', 'mensagem' => 'Importação concluída.']);
        } catch (\Exception $e) {
            DB::rollBack();
            return response()->json(['status' => 'erro', 'mensagem' => $e->getMessage()], 500);
        }
    }
}
