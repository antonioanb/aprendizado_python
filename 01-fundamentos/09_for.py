"""
ESTRUTURA FOR (Para cada...)
Ideal para percorrer sequências (iteráveis) como strings, listas e intervalos.
"""

# ---------------------------------------------------------
# 1. PERCORRENDO STRINGS (Iteração Básica)
# ---------------------------------------------------------
texto = "Python"

for letra in texto:
    print(f"Letra: {letra}")

# ---------------------------------------------------------
# 2. USANDO RANGE (Contagem Controlada)
# ---------------------------------------------------------
# range é uma função que gera um iteravel de numeros especificados, no caso ele está gerando numeros de 1 a 10 pois o range não entrega o ultimo
# range(inicio, fim_exclusivo) -> gera de 1 até 10
for i in range(1, 11):
    print(f"Número: {i}")

# ---------------------------------------------------------
# 3. LISTAS E CONTROLE DE FLUXO (Break vs Continue)
# ---------------------------------------------------------
frutas = ["banana", "maçã", "uva", "leite", "arroz"]

print("\n--- Buscando a uva ---")
for item in frutas:
    if item == "uva":
        print(f"Encontrado: {item}! Parando o loop. 🛑")
        break  # Interrompe o loop completamente
    print(f"Verificando: {item}...")

print("\n--- Pulando o número 3 ---")
for num in range(1, 6):
    if num == 3:
        print("Pulei o 3! 💨")
        continue  # Pula o restante desta volta e vai para a próxima
    print(f"Número atual: {num}")