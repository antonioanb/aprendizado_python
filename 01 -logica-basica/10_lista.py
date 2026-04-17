"""
LISTAS (Estruturas Mutáveis)
Uma lista armazena múltiplos valores em uma única variávell,
mantendo a ordem dos elementos através de índices.
"""

# ---------------------------------------------------------
# 1. ACESSO POR ÍNDICE
# ---------------------------------------------------------
frutas = ["Maçã", "Banana", "Uva"]

# Índices:   [0]      [1]      [2]
# Valores:  "Maçã"   "Banana"  "Uva"

print(f"Fruta na posição 0: {frutas[0]}")

# ---------------------------------------------------------
# 2. MUTABILIDADE (Troca de Apontamento)
# ---------------------------------------------------------
# O índice 1 deixa de apontar para "Banana" e aponta para "Morango"
frutas[1] = "Morango"

print(f"Lista atualizada: {frutas}")

# ---------------------------------------------------------
# 3. MATRIZES (Listas de Listas)
# ---------------------------------------------------------
# Imagine como coordenadas: [linha][coluna]
matriz = [
    [1, 2], # Linha 0
    [3, 4], # Linha 1
    [5, 6]  # Linha 2
]

# Acessando o valor 2 (Linha 0, Coluna 1)
print(f"Item na matriz[0][1]: {matriz[0][1]}")

# Acessando o valor 6 (Linha 2, Coluna 1)
print(f"Item na matriz[2][1]: {matriz[2][1]}")

