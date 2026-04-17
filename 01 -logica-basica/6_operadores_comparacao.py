"""
OPERADORES DE COMPARAÇÃO
Símbolos para fazer perguntas ao Python. 
O retorno é sempre Booleano (True/False).
"""

# TABELA DE REFERÊNCIA
# == (Igual)        | != (Diferente)
# >  (Maior)        | <  (Menor)
# >= (Maior/Igual)  | <= (Menor/Igual)

# ---------------------------------------------------------
# EXEMPLO 1: Igualdade (==) - Verificação de Acesso
# ---------------------------------------------------------
admin_sistema = "master"
admin_digitado = input("Digite o admin: ")

if admin_digitado == admin_sistema:
    print("Acesso concedido ✅")
else:
    print("Usuário inválido ❌")

# ---------------------------------------------------------
# EXEMPLO 2: Maior que (>) - Saúde
# ---------------------------------------------------------
temp = float(input("Qual a sua temperatura?: "))

if temp > 37.0:
    print(f"Temperatura {temp}°C: Está com febre 🤒")
else:
    print(f"Temperatura {temp}°C: Tudo normal 😀")

# ---------------------------------------------------------
# EXEMPLO 3: Maior ou Igual (>=) - Lotação
# ---------------------------------------------------------
vagas_ocupadas = int(input("Total de pessoas agora: "))
LIMITE = 9

if vagas_ocupadas >= LIMITE:
    print("Capacidade máxima atingida! 🚫")
else:
    print(f"Pode entrar. Vagas restantes: {LIMITE - vagas_ocupadas}")