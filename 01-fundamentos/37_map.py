#map é uma função embutida do python que permite aplicarr uma função a cada item de um iteravel, retornando um iteravel com os resultados.

produtos= [
    {'nome': 'detergente', 'preco': 10.99},
    {'nome': 'sabão em pó', 'preco': 25.50},
    {'nome': 'amaciente', 'preco': 15.75},
    {'nome': 'esponja', 'preco': 5.20},
]

#exemplo com listcomprehension---
precos_dobrados = [p['preco'] *2 for p in produtos]

print(list(precos_dobrados))

#agora usando map---
def dobrar_preco(produto):
    return produto['preco'] * 2

precos_dobrados = map(dobrar_preco, produtos)
print(list(precos_dobrados))

#usando função lambda---
precos_dobrados = map(lambda produto: produto['preco'] * 2, produtos)
print(list(precos_dobrados))