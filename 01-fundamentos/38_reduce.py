#reduce reduz um iteravel a um unico valor, aplicando uma função cumulativa aos itens do iteravel. diferente do map e filter, reduce retorna um unico valor e não um iteravel. para usar reduce é necessário importar a função do módulo functools.
import functools

#exemplo de uso do reduce para calcular o produto de uma lista de numeros
numeros = [1, 2, 3, 4, 5]   
def multiplicar(x, y):
    return x * y

produto = functools.reduce(multiplicar, numeros)
print(produto)