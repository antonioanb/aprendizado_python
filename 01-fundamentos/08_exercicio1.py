#Exercício: Simulador de Caixa Eletrônico
#Configuração Inicial: Crie uma variável saldo com um valor (ex: 1000.0) e uma variável senha_cadastrada (ex: "1234").
#Segurança (O Loop): O programa deve pedir a senha do usuário. Enquanto a senha digitada for diferente da senha_cadastrada, o programa deve dizer "Senha Incorreta" e pedir novamente.
#Menu de Opções: Assim que ele acertar a senha, o programa entra e pergunta: "Qual valor você deseja sacar?".
#A Decisão (O Coração do Código):

# SE o valor do saque for menor ou igual ao saldo E o valor for maior que 0:
# Subtraia o valor do saldo.
# Diga: "Saque realizado com sucesso!".
# Mostre o novo saldo.
# SENÃO SE o valor do saque for maior que o saldo:
# Diga: "Saldo insuficiente!". ##      Diga: "Valor inválido!".

saldo = 100.0
senha_cadastrada= "234"

while True:
    
    senha_digitada = input("digite a senha para entrar...")
    
    if senha_digitada != senha_cadastrada:
        print("senha invalida !!!")
    
    if senha_digitada == senha_cadastrada:
        valor_saque = float(input("qual valor deseja savar ?: "))
        
        if saldo >= valor_saque:
            saldo = saldo - valor_saque
            print("saque realizado com sucesso !!")
            print(f"saldo atual {saldo:.2f}")
            break #break  encerra o loop
        elif saldo < valor_saque:
            print("Saldo insuficiente ")
        else:
            print("valor invalido")   
            