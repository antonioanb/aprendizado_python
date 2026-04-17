# fatiamento é como se tirasse uma foto de uma seção especifica da lista para criar uma nova foto.

# exemplo de lista
# indices: 0    1    2    3    4
letras = ["A", "B", "C", "D", "E"]
#           [inicio:fim]
partes = letras[1:4] #pegando do indice 1 até antes do 4

# o indice fim nunca é incluido no resultado, para pegar o "E" teria que ir até o indice 5

print(partes)

#omitindo o inicio ou o fim
inicio = letras[:3]#pegando do inicio até o indice 2
fim = letras[2:]#pegando do indice 2 até o final

print(inicio)
print(fim)


#pulando
saltando = letras[0:5:2]#começando do 0 vai até o 5 pulando de 2 em 2
print(saltando)


