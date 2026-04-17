"""
   input =  é uma função de entrada de dados que pausa a execução do programa e fica esperando o usuario digitar algo, ele pode guardar o que foi digitado pelo usuario em uma variavel, e tudo que foi digitado é classificado como str.

   if = if(se) é uma estrutura condicional, ele faz o python executar um codigo caso a condição seja verdadeira. se não for ele pula esse bloco, mas se existir um else(se não) ele o executa.

"""


# ultilização de input
# como tudo que vem do input() é classifica como texto então nesse caso se a pessoa responder 25 o python vê isso como "25" um texto, e uma operação como "25" + 1 vai dar erro.
idade = input("Qual é a sua idade ? ")


# para resolver isso é preciso fazer conversão de tipos(Casting) que é trocar a "etiqueta" que o python coloca no valor para o tipo desejado.
idade = int(idade)

idade_somada = idade + 1

# print exibe um valor no terminal quando o codigo é executado
print(idade_somada)


# agora usando if. a baixo o print() só vai executar caso a idade for maior ou igual a 18, se não o bloco else é executado.
if idade >= 18:
    print("maior de idade 🧔🏻")

else:
    print("menor de idade 🧒🏻")
    



# elif (senão se): É o intermediário.
# Serve para testar uma nova condição caso a anterior tenha sido falsa.
# exemplo mais completo.

nota = int(input("Qual sua nota? "))

if nota >= 9:
    print("Excelente! 🏆")
elif nota >= 7:
    # O Python só chega aqui se a nota for menor que 9.
    print("Você passou! ✅")
elif nota >= 5:
    # O Python só chega aqui se a nota for menor que 7.
    print("Exame final... 📝")
else:
    # Se não for nenhuma das opções acima.
    print("Reprovado. ❌")

# o else é sempre o ultimo
