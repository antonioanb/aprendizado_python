# exemplo criando uma lista
lista1 = []

for numero in range(10):
    #pode inserir filtros ou calculos complexos aqui dentro do loop 
    lista1.append(numero)
print(f"for tradicional: {lista1}")

# fazendo a mesma coisa com list comprehension
# Sintaxe: [expressão for item in iterável]
list2 =[numero for numero in range(10)]
print(f"list comprehension: {list2}")

# O que está à esquerda do 'for' é o corpo do loop (o valor a ser inserido); 
# os [ ] já criam a lista e inserem os itens, dispensando o uso de .append(). porque o processo já está sendo feito dentro da lista.
#a esqueda é possivel colocar até funções o que torna a list comprehension muito poderosa, mas o mais comum é colocar expressões simples como no exemplo acima.

# list comprehension também podem ser usadas para filtrar, basta colocar a condição depois do 'for'
list3 = [numero for numero in range(10) if numero % 2 == 0]
print(f"list comprehension com filtro: {list3}")

# tambem é possivel fazer mapeamentos com list comprehension, ou seja, aplicar uma função a cada item da lista. basta colocar a expressão que deseja aplicar a cada item à esquerda do 'for'
list4 = [numero * 2 for numero in range(10)]
print(f"list comprehension com mapeamento: {list4}")




