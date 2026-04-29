# exemplo simples de um afunção que executa outra função
def executar(f, *args):
    return f(*args)


#função que soma dois numeros
def somar_numeros(x, y):
    return x + y

#usando a função
print(executar(somar_numeros, 10, 20))

# agora fazendo o mesmo com uma função lambda
print(executar(lambda x, y: x + y, 3, 5))

#explicação
#sintaxe: executa(lambda parametros: corpo da função, argumentos)
#uma função lambda retorna automaticamente.
#não é regra mas uma função lambda quase sempre ém execurtada por outra função como a executar do exemplo. 