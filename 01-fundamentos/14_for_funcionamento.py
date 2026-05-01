# detalhando o funcionemento do for para melhor entendimento

# ok, o for pode percorrer um objeto iteravel e "pegar" um item por vez, mas para um oobjeto ser iteravel ele internamente precisa de um metodo, e metodo .__iter__(), todo o item iteravel tem esse metodo, pode ser verificado chamando ele com .__iter__()

# O Iterável: É a fonte de dados (ex: uma string, lista ou tupla).
# O Iterador: É o "entregador" que sabe qual é o próximo item.

nome = "antonio".__iter__()#chamando o metodo .__iter__()
print(nome) # retorna <str_ascii_iterator object at 0x790ce03e4a30> que é o iterador  e endereço onde ele está

# o iterator é o elemento que sabe entregar um elemento por vez.

texto = iter("esse é um iteravel") #.__iter__() tambem pode ser chamado com a funçãoo iter().

# nex, chama o proximo item do elemneto que está sendo iteravel
print(nome.__next__())
print(nome.__next__())
print(nome.__next__())
print(nome.__next__())
print(nome.__next__())
print(nome.__next__())
print(nome.__next__())
#print(nome.__next__())# quandoo todos os itens forem chamados o pyhton sobe um erro "StopIteration"

#.__next__() tambem pode ser chamado com a função next()

# sabendo disso dá para fazer um "for manual":

sobrenome = "barros"
iterator = iter(sobrenome)

while True:
    
    try:
        print(next(iterator))

    except StopIteration: 
        break 




