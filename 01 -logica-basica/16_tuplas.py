"""
TUPLAS (tuple)
Estruturas de dados imutáveis. Uma vez criadas, não podem ser alteradas 
(não possuem append, remove ou atribuição por índice).
"""

# ---------------------------------------------------------
# 1. CRIAÇÃO E SINTAXE
# ---------------------------------------------------------
# Podem ser criadas com ou sem parênteses (a vírgula é o que define)
nomes = ("eduardo", "carlos", "joão")
cores = "azul", "verde", "amarelo" # Também é uma tupla!

# O CASO ESPECIAL: Tupla de um único item
tupla_real = ("valor",)  # Correto
apenas_str = ("valor")   # Errado: O Python lê como uma string entre parênteses

# ---------------------------------------------------------
# 2. CONVERSÃO (Casting)
# ---------------------------------------------------------
lista_frutas = ["Maçã", "Pera"]
tupla_frutas = tuple(lista_frutas) # Útil para "proteger" os dados da lista

# ---------------------------------------------------------
# 3. POR QUE USAR? (Vantagens)
# ---------------------------------------------------------
# - Segurança: Garante que os dados não serão alterados por erro.
# - Performance: São levemente mais rápidas que listas.
# - Uso como Chaves: Podem ser usadas como chaves em dicionários (listas não).

print(f"Tipo do único item: {type(tupla_real)}")