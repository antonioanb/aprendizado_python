"""
UNPACKING (Desempacotamento)
Técnica para extrair valores de iteráveis diretamente para variáveis.
"""

# ---------------------------------------------------------
# 1. DESEMPACOTAMENTO DIRETO (Exige número exato)
# ---------------------------------------------------------
nomes = ["antonio", "carlos", "miguel"]
n1, n2, n3 = nomes

# ---------------------------------------------------------
# 2. USANDO O * RESTO (Coletor)
# ---------------------------------------------------------
# O '*' transforma o restante em uma nova lista.
primeiro, *resto = ["davi", "rita", "leandro", "jose"]
# primeiro -> "davi"
# resto    -> ["rita", "leandro", "jose"]

# ---------------------------------------------------------
# 3. OMITINDO VALORES (Convenção '_')
# ---------------------------------------------------------
# Pegando apenas o primeiro e o terceiro, ignorando o resto
n1, _, n3, *_ = ["ana", "beatriz", "caio", "duda", "elaine"]

print(f"Selecionados: {n1} e {n3}")