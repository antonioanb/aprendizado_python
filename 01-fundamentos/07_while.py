""" while é uma estrutura de repetição(loop), ele é como um if teimoso que não desiste de executar um bloco de codigo enquanto a condição for verdadeira.
"""
"""
ESTRUTURA WHILE (O "if teimoso")
Executa um bloco de código repetidamente ENQUANTO a condição for True.
"""

# ---------------------------------------------------------
# 1. LOOP COM CONTADOR (Repetição Controlada)
# ---------------------------------------------------------
contador = 1

while contador <= 5:
    print(f"Repetição nº {contador}")
    # Atalho para: contador = contador + 1
    contador += 1 

#Sempre certifique-se de que algo dentro do bloco vai eventualmente tornar a condição falsa, se não vai entrar em loop infinito repetindo até o computador travar ou o codigo for encerrado manualmente.


# ---------------------------------------------------------
# 2. VALIDAÇÃO DE ENTRADA (Repetição Indeterminada)
# ---------------------------------------------------------
SENHA_MESTRE = "1234"
tentativa = ""

while tentativa != SENHA_MESTRE:
    tentativa = input("Digite a senha para acessar o sistema: ")
   
    if tentativa != SENHA_MESTRE:
        print("Senha incorreta! Tente novamente. ❌")

print("Acesso concedido! Bem-vindo. ✅")


#while é otimo para validar entradas, Exemplo: obrigar o usuario a digitar a senha correta para continuar


    