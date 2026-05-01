"""
FUNÇÕES (def)
Blocos de código reutilizáveis que executam ações específicas.
Ajudam a evitar repetição (princípio DRY - Don't Repeat Yourself).
"""

# ---------------------------------------------------------
# 1. PARÂMETROS E ARGUMENTOS
# ---------------------------------------------------------
# Parâmetro: Nome definido na criação da função (ex: nome, idade)
# Argumento: Valor real passado na chamada (ex: "Antonio", 36)

def saudar(nome, idade):
    print(f"Olá {nome}, você tem {idade} anos.")

saudar("Antonio", 36)

# ---------------------------------------------------------
# 2. VALORES PADRÃO (Default)
# ---------------------------------------------------------
# Importante: Parâmetros com padrão devem vir por ÚLTIMO.
def conexao(ip, porta=8080):
    print(f"Conectando ao IP {ip} na porta {porta}")

conexao("192.168.0.1") # Usa a porta 8080 automática

# ---------------------------------------------------------
# 3. RETORNO (O "produto final" da função)
# ---------------------------------------------------------
def calcular_area_circulo(raio):
    return 3.1415 * (raio ** 2)

area = calcular_area_circulo(5)
print(f"Área: {area:.2f}") # Exibindo com 2 casas decimais

# ---------------------------------------------------------
# 4. DOCUMENTAÇÃO (Docstrings)
# ---------------------------------------------------------
def soma(x, y):
    """Soma dois números e retorna o resultado."""
    return x + y

# Funções devem fazer UMA coisa bem feita. Se uma função está fazendo muitas coisas diferentes, deve ser divida em funções menores.