import json


def carregarJson(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)


grade = carregarJson("grade.json")
blocos = carregarJson("blocos_aula.json")


#transformando a disciplina na k para o dic
blocos = {
    bloco["disciplina"]: bloco
    for bloco in blocos
}
print(blocos)

""" print("Grade:")
print(json.dumps(grade, indent=2, ensure_ascii=False)) """

"""
print("\nBlocos:")
print(json.dumps(blocos, indent=2, ensure_ascii=False))
 """
