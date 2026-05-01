import copy

"""
MÉTODOS DE DICIONÁRIO E CÓPIAS
Ferramentas para extrair dados e gerenciar como o Python lida com a memória.
"""

pessoa = {
    "nome": "Antonio",
    "sobrenome": "Barros",
    "interesses": ["Python", "NixOS"], # Item mutável para testar a cópia
}

# ---------------------------------------------------------
# 1. ACESSO E ITERAÇÃO
# ---------------------------------------------------------
# .keys()   -> Somente as chaves
# .values() -> Somente os valores
# .items()  -> Pares (chave, valor) - Perfeito para o for!

for chave, valor in pessoa.items():
    print(f"{chave.upper()}: {valor}")

# setdefault: Garante que a chave exista sem dar erro
pessoa.setdefault("idade", 0)

# ---------------------------------------------------------
# 2. O PROBLEMA DA CÓPIA (shallow vs deep)
# ---------------------------------------------------------

# CÓPIA RASA (Shallow Copy)
# Copia o dicionário, mas a lista 'interesses' ainda é a MESMA na memória.
rasa = pessoa.copy()
rasa["interesses"].append("Linux") # Isso vai alterar 'pessoa' também!

# CÓPIA PROFUNDA (Deep Copy)
# Cria um novo dicionário E uma nova lista em endereços diferentes.
profunda = copy.deepcopy(pessoa)
profunda["interesses"].append("Docker") # Agora 'pessoa' está protegida.