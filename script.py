import pandas as pd
import json

def gerarBlocosAulas(nomeArquivo):
    xls = pd.ExcelFile(nomeArquivo)
    df = xls.parse('Disciplinas oferta 2024.1')

    df = df.rename(columns={
        'COD. DISCIPLINA': 'codigo_disciplina',
        'DISCIPLINA': 'nome_disciplina',
        'CH': 'ch',
        df.columns[6]: 'professor',
        'PERIODO': 'periodo',
        'TURMA': 'turma',
        'AMBIENTE (Relacionar os ambientes específicos)': 'ambiente'
    })

    df = df.dropna(subset=['codigo_disciplina', 'nome_disciplina', 'professor'])

    blocosNecessariosPorOferta = []

    for i, row in df.iterrows():
        ch = row['ch']
        blocos = int(round(ch / 20))
        if blocos == 0:
            continue

        oferta = {
            'disciplina': row['codigo_disciplina'],
            'nomeDisciplina': row['nome_disciplina'],
            'professor': row['professor'],
            'turma': str(row['turma']).split(" ")[0],
            'periodo': row['periodo'],
            'ambiente': row['ambiente'],
            'blocosNecessarios': blocos,
            'alocacao': []
        }

        blocosNecessariosPorOferta.append(oferta)

    return blocosNecessariosPorOferta


if __name__ == "__main__":
    arquivo = "PLANEJAMENTO_2024_1_FGGCOMP.xlsx"
    blocos = gerarBlocosAulas(arquivo)

    with open("blocos_aula.json", "w", encoding="utf-8") as f:
        json.dump(blocos, f, indent=2, ensure_ascii=False)
