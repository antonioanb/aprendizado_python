# desempacotamento de dicionario

pessoa = {"nome": "Antonio", "sobrenome": "Barros"}

dados_pesoas = {"idade": 36, "profissão": "programador"}

# desempacotando as informações em um unico dicionario
pessoa_completa = {**pessoa, **dados_pesoas, "profissão":"desenvolvedor Django","genero": "masculino"}

print(pessoa_completa)


# ------------------------------
# kwargs = keyword arguments (argumentos nomeados)
# com kwargs a função pode receber chave e valor via argumentos nomeados
# ------------------------------
def mostrar_argumentos(*args, **kwargs):
    #argumentos não nomeados vão para args
    for a in args:
        print(a)

    # parametros nomeados vão para kwargs que é um dicionario
    for chave, valor in kwargs.items():
        print(f"chave: {chave} valor: {valor}")


mostrar_argumentos(**pessoa_completa)
mostrar_argumentos("python", "c++" ,"java")


# no exemplom eu desempacoto um dicionario em uma função
configuracoes = {
    "placa_mae": "ASUS TUF Gaming B550M",
    "processador": "AMD Ryzen 5 5600X",
    "memoria": "16 GB DDR4 3200MHz",
    "placa_de_video": "NVIDIA RTX 3060 12GB",
    "armazenamento": "SSD 1TB NVMe",
    "monitor": "LG 24'' 144Hz Full HD",
    "fonte": "Corsair 650W 80 Plus Bronze",
    "gabinete": "Cooler Master Q300L",
    "sistema": "Windows 11",
}

mostrar_argumentos(**configuracoes)