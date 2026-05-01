"""
ITERAÇÃO COM FOR E ENUMERATE
Como percorrer sequências acessando o valor e sua posição (índice).
"""

frutas = ["maçã", "banana", "abacaxi", "laranja"]

# ---------------------------------------------------------
# 1. ITERAÇÃO SIMPLES (Apenas valores)
# ---------------------------------------------------------
# 'fruta' é a etiqueta temporária que aponta para o item atual
for fruta in frutas:
    print(f"Fruta atual: {fruta}")

# ---------------------------------------------------------
# 2. ITERAÇÃO COM ÍNDICE (Enumerate)
# ---------------------------------------------------------
# O enumerate() entrega uma TUPLA contendo (índice, valor) a cada volta.
# Usamos o 'desempacotamento' para jogar cada um em sua variável.

for indice, fruta in enumerate(frutas):
    print(f"[{indice}] -> {fruta}")

# DICA: Você pode começar o índice de um número específico (ex: 1)
# for indice, fruta in enumerate(frutas, start=1):
#     print(f"Item nº {indice}: {fruta}")