# Sistema de Geração de Blocos de Aula para Alocação com Busca Tabu

Este projeto tem como objetivo processar os dados de planejamento de disciplinas de um curso e preparar uma estrutura que permita alocar essas aulas de forma otimizada, utilizando um algoritmo de Busca Tabu.

## Estrutura dos dados de entrada

O sistema lê um arquivo Excel com a aba `Disciplinas oferta 2024.1`. A planilha deve conter as seguintes colunas:

- COD. DISCIPLINA
- DISCIPLINA
- CH (carga horária)
- PROFESSOR
- PERIODO
- TURMA
- AMBIENTE
- RESTRIÇÕES (formato livre ou estruturado como JSON, dependendo do uso)

Exemplo de entrada:

| COD. DISCIPLINA | DISCIPLINA | CH  | PROFESSOR              | TURMA       | PERIODO | AMBIENTE                  | RESTRIÇÕES                                 |
|------------------|------------|-----|-------------------------|-------------|---------|----------------------------|---------------------------------------------|
| FGGCOMP.004       | Cálculo I   | 90  | Karina Pereira Carvalho | 2024-01-01 | 1       | Sala de Aula              | Não disponível Segunda 13:30 e Sexta 08:00 |

---

## Horários possíveis

A grade de horários é composta por 4 blocos fixos por dia:

- 08:00–10:00  
- 10:20–12:20  
- 13:30–15:30  
- 15:50–17:50

Dias considerados: Segunda a Sexta.  
Total: **5 dias × 4 blocos = 20 blocos de aula por semana**

---

## Lógica de divisão por blocos

Cada disciplina é alocada em blocos de 2h (blocos casados). A quantidade de blocos é baseada na carga horária (CH):

- Uma disciplina de 60h → 2 blocos
- Uma disciplina de 90h → 3 blocos

O script `gerar_blocos_aulas.py` faz esse cálculo automaticamente e gera estruturas como:

```python
{
    "disciplina": "FGGCOMP.004",
    "nomeDisciplina": "Cálculo I",
    "professor": "Karina Pereira Carvalho",
    "turma": "2024-01-01",
    "periodo": 1,
    "ambiente": "Sala de Aula",
    "blocosNecessarios": 3,
    "alocacao": []
}
