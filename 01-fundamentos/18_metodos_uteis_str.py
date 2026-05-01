# split = metodo que divide uma string em uma lista
# separa a string se baseando em um caractere especifico

frase = "olha só que, coisa interessante, esses metodos"

listar_frase = frase.split(",") #serapar em cada ","

print(listar_frase)#['olha só que', ' coisa interessante', ' esses metodos']

#limitando o numero de divisões
email = "antoniodev@email.com.br"
email_dividido = email.split(".",1) #só vai dividir no primeiro "." que encontrar
print(email_dividido)#['antoniodev@email', 'com.br']


#join = une uma lista em uma string

lista1 = ["python", "é", "legal"]
frase1 = " ".join(lista1)#unindo a lista separando por espaço
print(frase1)#python é legal

#uso interessante, criando um caminho
lista2 = ["home", "musicas", "lançamentos", "2026"]
caminho_diretorio = "/".join(lista2)
print(f"Diretorio: {caminho_diretorio}")#Diretorio: home/musicas/lançamentos/2026

#alterando uma string...
frase_original = "Eu gosto de programar em python"

#transformar em lista
frase_lista = frase_original.split()

#alterando elementos da lista
frase_lista[0] = "Nós"
frase_lista[1] = "gostamos"

#mudando de volta para string
frase_modificada = " ".join(frase_lista)

#resultado
print(frase_modificada)#Nós gostamos de programar em python