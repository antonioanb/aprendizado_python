# importações necesssarias, itertools é um módulo da biblioteca padrão do Python que fornece funções para criar iteradores eficientes para operações de combinação, permutação e produto cartesiano.
from itertools import permutations, combinations, product

#listas para teste
nomes = ["Antonio", "Maria", "João"]

camisetas = [
    ["preta", "branca"],
    ["p", "m", "g"],
    ["masculina", "feminina"],
    ["algodão", "sintetico"],]

#gerando permutações de nomes, onde a ordem importa. ["Antonio", "Maria"] é diferente de ["Maria", "Antonio"].
print(*list(permutations(nomes, 2)), sep="\n")

print("-" * 20)
#gerando combinações de nomes, onde a ordem não importa. ["Antonio", "Maria"] é igual a ["Maria", "Antonio"].
print(*list(combinations(nomes, 2)), sep="\n")

print("-" * 20)
#gerando o produto cartesiano de camisetas, onde a ordem importa e elementos podem se repetir.
print(*list(product(*camisetas)), sep="\n")