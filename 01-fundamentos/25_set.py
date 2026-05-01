# SET: Coleção não ordenada de elementos únicos (ideal para remover duplicatas e testes de pertinência).

# CARACTERÍSTICAS:
# 1. Não Ordenado: Itens não possuem índice; a posição na memória é arbitrária.
# 2. Elementos Únicos: Descarta automaticamente entradas repetidas.
# 3. Mutável, mas com restrições: O set pode crescer/diminuir, mas seus itens devem ser imutáveis (hashable).
# 4. Não Indexável: Não suporta fatiamento ou acesso por posição (ex: s[0]).

frutas = {"maça", "banana", "morango", "figo"}
print(frutas) 



# MÉTODOS PRINCIPAIS
s1 = set()

s1.add(1)                        # Insere um único elemento.
s1.update(("Antonio", 100, 200)) # Insere múltiplos elementos (iteráveis) de uma vez.
s1.discard("Antonio")            # Remove um item se ele existir; não gera erro caso contrário.
# s1.remove("X")                 # Semelhante ao discard, mas gera erro se o item não existir.
# s1.clear()                     # Esvazia o conjunto completamente..

print(f"Set atual: {s1}")



# OPERAÇÕES MATEMÁTICAS (ÁLGEBRA DE CONJUNTOS)
set1 = {1, 2, 3}
set2 = {2, 3, 4}

# União (|): Combina todos os itens de ambos, sem duplicatas.
set3 = set1 | set2
print(f"União: {set3}")

# Interseção (&): Apenas os elementos presentes em ambos os conjuntos.
set3 = set1 & set2
print(f"Interseção: {set3}")

# Diferença (-): Itens presentes no set da esquerda que NÃO estão no da direita.
print(f"Diferença (1-2): {set1 - set2}") # Retorna {1}
print(f"Diferença (2-1): {set2 - set1}") # Retorna {4}

# Diferença Simétrica (^): Itens que estão em um ou outro, mas NÃO em ambos.
set3 = set1 ^ set2
print(f"Diferença Simétrica: {set3}") # Retorna {1, 4}