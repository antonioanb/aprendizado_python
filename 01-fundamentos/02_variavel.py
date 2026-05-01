"""uma variavel é um nome ou uma etiqueta que aponta para um endereço de memoria onde um valor literal(valor real) está guardado.
  imaginando que na memoria ram do computador existem varias "caixas", nessas "caixas" é possivel guardar valores literais como numeros textos e outros, cada caixa tem um endereço especifico, para podermos acessar esses endereços criamos um nome que aponta para o endereço é isso que chamamos de variavel.
  
  valor_guardado_na_memoria: valor literal 

  endereço_da_memoria: local fisico na memoria ram onde o valor está 
 
  nome_da_variavel: nome simbolico que aponta para o endereço

  valor_guardado_na_memoria -> endereço_da_memoria = 👈🏻 nome_da_variavel 
"""

# com isso é possivel guardar e recuperar valores na memoria do computador, exemplo real:
nome = "antonio" 

# O que acontece nos bastidores:
# 1. O Python cria o valor literal "Antonio".
# 2. Como ele vê as aspas, ele já classifica esse valor como tipo 'str'.
# 3. Ele coloca esse valor em um endereço (ex: 0xABC).
# 4. Ele faz o nome 'nome' apontar para 0xABC.

# a variavel não se importa com o tipo do valor ela apenas aponta para o endereço, quem tem o tipo é o valor que está lá dentro, por isso python tem tipagem dinamica, o que quer dizer que dá para fazer a variavel apontar para outro local da memoria, exemplo:
nome = 10 # a etiqueta nome parou de apontar para o texto e agora aponta para um numero.

# variavel não é a caixa ela é o dedo que aponta para a caixa 👈🏻
# diferente de outras linguagens de tipagem estatica como c e java é possivel mudar pra onde ela aponta. 

idade = 25 

idade = "python" # variavel que antes apontava para 25 agora aponta para "python"

# nesse caso o valor literal 25 ficou sozinho na memoria sem ninguem apontar para ele, quando isso acontace o pyhton usa um sistema chamado Garbage Collector (Coletor de Lixo) que limpa da memoria coisas não usadas para liberar espaço.


# também é possivel armazenar operações matematicas, o python primeiro resolve a conta e depois aponta para o resultado

ano_nascimento = 1999

salario = 2_000.0

idade_atual = 2025 - ano_nascimento





