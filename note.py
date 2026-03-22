from typing import Dict, List, Tuple

# Definição das restrições e suas penalidades (quanto menor, pior)
RESTRICOES = {
    "conflito_professor": -10,      # Dois blocos do mesmo professor no mesmo horário
    "conflito_turma": -8,           # Dois blocos da mesma turma no mesmo horário
    "conflito_ambiente": -6,        # Dois blocos no mesmo ambiente no mesmo horário
    "blocos_consecutivos": -2,      # Mais de 2 blocos consecutivos para o mesmo professor/turma
    "dispersao_blocos": -1,         # Blocos de uma disciplina muito dispersos na semana
    "horario_ruim": -3,             # Bloco alocado em horário pouco desejado (ex: última faixa do dia)
    # Adicione outras restrições conforme necessário
}

def avaliar_grade(grade: Dict) -> Tuple[int, Dict[str, int]]:
    """
    Avalia a grade de horários, retornando uma nota total e um detalhamento das violações.
    Espera um dicionário no formato de grade_por_horario.json.
    """
    nota_total = 0
    violacoes = {k: 0 for k in RESTRICOES}

    # Índices auxiliares para checagem rápida
    for dia, blocos in grade.items():
        for horario, alocacoes in blocos.items():
            professores = set()
            turmas = set()
            ambientes = set()
            for aloc in alocacoes:
                prof = aloc.get("professor")
                turma = aloc.get("turma")
                ambiente = aloc.get("ambiente")
                # Conflito de professor
                if prof in professores:
                    violacoes["conflito_professor"] += 1
                else:
                    professores.add(prof)
                # Conflito de turma
                if turma in turmas:
                    violacoes["conflito_turma"] += 1
                else:
                    turmas.add(turma)
                # Conflito de ambiente
                if ambiente in ambientes:
                    violacoes["conflito_ambiente"] += 1
                else:
                    ambientes.add(ambiente)
                # Horário ruim (exemplo: última faixa do dia)
                if horario == "15:50":
                    violacoes["horario_ruim"] += 1

    # Exemplo de checagem de blocos consecutivos (simplificado)
    # Você pode expandir para analisar blocos consecutivos por professor/turma
    # e dispersão de blocos ao longo da semana

    # Cálculo da nota total
    for restricao, peso in RESTRICOES.items():
        nota_total += violacoes[restricao] * peso

    return nota_total, violacoes

# Exemplo de uso:
# from restricoes import avaliar_grade
# import json
# with open("grade_por_horario.json") as f:
#     grade = json.load(f)
# nota, detalhes = avaliar_grade(grade)
# print("Nota:", nota)
# print("Detalhes:", detalhes)