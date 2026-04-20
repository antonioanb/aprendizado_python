"""
EXERCÍCIO: Sistema de Perguntas e Respostas
Objetivo: Praticar iteração de dicionários e listas aninhadas.
"""

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qt_acertos = 0
qt_erros = 0

for pergunta in perguntas:
    print(f"Pergunta: {pergunta['Pergunta']}")
    op = pergunta["Opções"]

    for i, o in enumerate(op):
        print(f"{i}) {o}")

    escolha = input("-> ")

    acertou = False
    if escolha.isdigit():
        escolha_int = int(escolha)

        if escolha_int >= 0 and escolha_int < len(op):
            if op[escolha_int] == pergunta["Resposta"]:
                acertou = True
    
    if acertou:
        qt_acertos += 1
        print("Acertou")
    else:
        qt_erros += 1
        print(f"Errou, poxa a resposta corrata era {pergunta["Resposta"]}")

print(f"acertos: {qt_acertos} e erroou {qt_erros} de {len(perguntas)}")
