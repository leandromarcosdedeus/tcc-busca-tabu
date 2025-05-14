import json
import random

def carregarBlocos(caminhoEntrada):
    with open(caminhoEntrada, "r", encoding="utf-8") as f:
        return json.load(f)

def salvarGrade(grade, caminhoSaida):
    with open(caminhoSaida, "w", encoding="utf-8") as f:
        json.dump(grade, f, indent=2, ensure_ascii=False)

def temConflito(agendaProfessor, dia, hora, horarios):
    indice = horarios.index(hora)
    anterior = horarios[indice - 1] if indice > 0 else None
    seguinte = horarios[indice + 1] if indice < len(horarios) - 1 else None
    blocosDia = agendaProfessor.get(dia, [])
    return anterior in blocosDia or seguinte in blocosDia

def gerarGrade(blocosAula):
    dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
    horarios = ["08:00", "10:20", "13:30", "15:50"]
    blocosHorarios = [{"dia": d, "hora": h} for d in dias for h in horarios]

    agendaProfessores = {}
    agendaOcupada = set()

    for item in blocosAula:
        professor = item["professor"]
        if professor not in agendaProfessores:
            agendaProfessores[professor] = {}

        alocacao = []
        tentativas = 0
        while len(alocacao) < item["blocosNecessarios"] and tentativas < 500:
            bloco = random.choice(blocosHorarios)
            chave = (item["turma"], bloco["dia"], bloco["hora"])
            if chave in agendaOcupada:
                tentativas += 1
                continue
            if temConflito(agendaProfessores[professor], bloco["dia"], bloco["hora"], horarios):
                tentativas += 1
                continue
            alocacao.append(bloco)
            agendaOcupada.add(chave)
            agendaProfessores[professor].setdefault(bloco["dia"], []).append(bloco["hora"])
            tentativas = 0
        item["alocacao"] = alocacao
    return blocosAula

def gerarGradePorHorario(grade):
    gradePorHorario = {
        dia: {hora: [] for hora in ["08:00", "10:20", "13:30", "15:50"]}
        for dia in ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
    }

    for item in grade:
        for bloco in item["alocacao"]:
            dia = bloco["dia"]
            hora = bloco["hora"]
            alocado = {
                "disciplina": item["disciplina"],
                "nomeDisciplina": item["nomeDisciplina"],
                "professor": item["professor"],
                "turma": item["turma"],
                "periodo": item["periodo"],
                "ambiente": item["ambiente"]
            }
            gradePorHorario[dia][hora].append(alocado)
    
    return gradePorHorario




if __name__ == "__main__":
    caminhoEntrada = "blocos_aula.json"
    caminhoSaida = "grade_horarios_restrita.json"

    blocosAula = carregarBlocos(caminhoEntrada)
    gradeGerada = gerarGrade(blocosAula)
    salvarGrade(gradeGerada, caminhoSaida)


    gradePorHorario = gerarGradePorHorario(gradeGerada)
    salvarGrade(gradePorHorario, "grade_por_horario.json")
