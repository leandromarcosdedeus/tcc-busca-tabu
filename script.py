import pandas as pd

def gerar_blocos_aulas(nome_arquivo):
    xls = pd.ExcelFile(nome_arquivo)
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

    blocos_necessarios_por_oferta = []

    for _, row in df.iterrows():
        ch = row['ch']
        blocos = int(round(ch / 20))  
        if blocos == 0:
            continue

        oferta = {
            'disciplina': row['codigo_disciplina'],
            'nome_disciplina': row['nome_disciplina'],
            'professor': row['professor'],
            'turma': str(row['turma']).split(" ")[0],
            'periodo': row['periodo'],
            'ambiente': row['ambiente'],
            'blocos_necessarios': blocos,
            'alocacao': []  
        }

        blocos_necessarios_por_oferta.append(oferta)

    return blocos_necessarios_por_oferta


if __name__ == "__main__":
    arquivo = "PLANEJAMENTO_2024_1_FGGCOMP.xlsx"
    blocos = gerar_blocos_aulas(arquivo)

    print("Exemplo de blocos gerados:")
    for item in blocos[:3]:
        print(item)
