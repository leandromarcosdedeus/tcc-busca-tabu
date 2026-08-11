import json


DIAS = [
    "segunda",
    "terca",
    "quarta",
    "quinta",
    "sexta",
    "sabado",
    "domingo"
]


HORARIOS = {
    "matutino": [
        ("08:00", "09:40"),
        ("10:00", "11:40")
    ],

    "vespertino": [
        ("13:00", "14:40"),
        ("15:00", "16:40"),
        ("16:40", "18:20")
    ],

    "noturno": [
        ("18:40", "20:20"),
        ("20:30", "22:10")
    ]
}


def gerarGrade():
    grade = []

    for periodo, horarios in HORARIOS.items():

        for dia in DIAS:

            for inicio, fim in horarios:

                bloco = {
                    "periodo": periodo,
                    "dia": dia,
                    "inicio": inicio,
                    "fim": fim,
                    "alocacao": None
                }

                grade.append(bloco)

    return grade


def salvarGrade(grade, caminhoSaida):
    with open(caminhoSaida, "w", encoding="utf-8") as f:
        json.dump(
            grade,
            f,
            indent=2,
            ensure_ascii=False
        )


grade = gerarGrade()

salvarGrade(
    grade,
    "grade.json"
)
