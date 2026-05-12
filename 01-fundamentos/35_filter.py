#filter é uma função do python que permite filtar itens de um iteravel com base em uma função que retorna True ou False. esse metodo retorna um iteravel com itens que satasfazem a condição definida na função de filtragem. diferente do listcomprehension, filter retorna um iteravel e não uma lista, por isso é necessário converter para lista usando list() ou usar um loop para iterar sobre os resultados.
produtos= [
    {'nome': 'detergente', 'preco': 10.99},
    {'nome': 'sabão em pó', 'preco': 25.50},
    {'nome': 'amaciente', 'preco': 15.75},
    {'nome': 'esponja', 'preco': 5.20},
]

#exemplo com listcomprehension---
produtos_filtrados = [p for p in produtos if p['preco'] > 15]

print(produtos_filtrados)

#agora usando filter---
# criando função de filtragem
def filtrar_produtos(produto):
    return produto['preco'] > 15

produtos_filtrados = filter(filtrar_produtos, produtos)
print(list(produtos_filtrados))

#usando função lambda---
produtos_filtrados = filter(lambda produto: produto['preco'] > 15, produtos)
print(list(produtos_filtrados))

#sintaxe do filter filter(função_de_filtragem, iteravel)
