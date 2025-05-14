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

Exemplo de entrada:

| COD. DISCIPLINA | DISCIPLINA         | CH  | PROFESSOR              | TURMA       | PERIODO | AMBIENTE                    |
|------------------|---------------------|------|--------------------------|--------------|----------|-------------------------------|
| FGGCOMP.004       | Cálculo I             | 90  | Karina Pereira Carvalho | 2024-01-01 | 1        | Sala de Aula                |

---

## Horários possíveis

A grade de horários é formada por 4 blocos fixos por dia:

- 08:00–10:00
- 10:20–12:20
- 13:30–15:30
- 15:50–17:30

Os dias da semana considerados são: Segunda, Terça, Quarta, Quinta e Sexta.

Assim, existem 20 blocos de aula possíveis por semana (5 dias × 4 blocos).

---

## Lógica de divisão por blocos

Cada disciplina será alocada em blocos de 2h. A conversão é feita com base na carga horária total (CH) da disciplina.

Exemplo:
- Uma disciplina de 60h precisa de 3 blocos semanais.
- Uma de 90h precisa de 5 blocos.

O script `gerar_blocos_aulas.py` calcula isso automaticamente e gera uma estrutura como:

```python
{
    'disciplina': 'FGGCOMP.004',
    'nome_disciplina': 'Cálculo I',
    'professor': 'Karina Pereira Carvalho',
    'turma': '2024-01-01',
    'periodo': 1,
    'ambiente': 'Sala de Aula',
    'blocos_necessarios': 5,
    'alocacao': []  
}
