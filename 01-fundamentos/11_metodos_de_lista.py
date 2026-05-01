"""
MÉTODOS DE LISTA
Funções internas para manipular a estrutura e os dados das listas.
"""

nomes = ["antonio", "carlos", "gabriel"]

# ---------------------------------------------------------
# 1. ADIÇÃO (Append vs Insert)
# ---------------------------------------------------------
# Adiciona ao final (O(1) - rápido)
nomes.append("beatriz") 

# Adiciona no índice 1 e "empurra" o resto (mais custoso para a memória)
nomes.insert(1, "davi") 

# ---------------------------------------------------------
# 2. REMOÇÃO (Pop vs Remove)
# ---------------------------------------------------------
# Remove por índice e retorna o valor (útil para desfazer ações)
removido = nomes.pop(1) 

# Remove a primeira ocorrência do valor literal
nomes.remove("gabriel") 

# ---------------------------------------------------------
# 3. ORGANIZAÇÃO E UTILITÁRIOS
# ---------------------------------------------------------
numeros = [5, 2, 9, 1]

# Ordena a lista original (In-place)
numeros.sort() 

# Busca a posição de um elemento
posicao_do_cinco = numeros.index(5) 

# Função global que conta quantos itens existem
tamanho = len(numeros) 

# ---------------------------------------------------------
# 4. LIMPEZA TOTAL
# ---------------------------------------------------------
# Esvazia a lista; itens sem ponteiros -> Garbage Collector 🗑️
nomes.clear()

# obs, sort() e append() alteram a lista diretamente na memoria, eles não criam uma nova lista, eles mexem na mesma que a variavel está apontando.

























































