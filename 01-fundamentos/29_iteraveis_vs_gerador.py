import sys
# ireraveis são objetos que podem ser percorridos item por item, como listas, tuplas, dicionários, conjuntos e strings. Eles armazenam todos os seus itens na memória, o que pode ser problemático para grandes volumes de dados.
lista = [ item for item in range(1000000) ] # isso pode consumir muita memória

# geradores (generators) são uma alternativa mais eficiente para iteráveis grandes. Eles produzem os itens sob demanda, ou seja, geram um item por vez e não armazenam toda a sequência na memória.
gerador = ( item for item in range(1000000) ) # isso é um gerador, não consome muita memória

# para acessar os itens de um gerador, podemos usar a função next()
print(next(gerador)) # isso retorna o próximo item do gerador, no caso 0
print(next(gerador)) # isso retorna o próximo item do gerador, no caso 1    
print(next(gerador)) # isso retorna o próximo item do gerador, no caso 2

# também podemos usar um loop para percorrer os itens de um gerador
for item in gerador:
    print(item) # isso imprime os itens do gerador, começando do 3 até 999999   

# geradores não armazenam nada, ele é um objeto iteravel que "lembra" o ultimo estado, ou seja a posição do ultimo item gerado.

# comparação de memória entre iteráveis e geradores
print(f"tamanho da lista: {sys.getsizeof(lista)} bytes") # isso mostra o tamanho da lista em bytes
print(f"tamanho do gerador: {sys.getsizeof(gerador)} bytes") # isso mostra o tamanho do gerador em bytes, que é muito menor que o da lista

