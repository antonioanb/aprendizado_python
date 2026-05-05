# uma função geradora é uma função que pode ser pausada e retomada, permitindo a geração de uma sequência de valores ao longo do tempo, em vez de calcular todos os valores de uma vez e armazená-los na memória.
# a palavra-chave yield é usada para produzir um valor e pausar a execução da função, permitindo que ela seja retomada posteriormente. Quando a função é chamada novamente, ela continua a partir do ponto onde foi pausada, mantendo seu estado interno.


def geradora():

    yield 1
    print("Depois do primeiro yield")
    yield 2
    print("Depois do segundo yield")        
    yield 3
    print("Depois do terceiro yield")

    return "Acabou" 


#gen vai gerar um objeto iterador, que pode ser percorrido usando um loop ou a função next() para obter os valores gerados.
gen = geradora()

print(next(gen))  # Imprime 1
print(next(gen))  # Imprime 2
print(next(gen))  # Imprime 3
#print(next(gen))  # Levanta StopIteration com a mensagem "Acabou"

# a função geradora é útil para trabalhar com grandes conjuntos de dados ou fluxos de dados infinitos, pois permite que os valores sejam gerados sob demanda, economizando memória e melhorando a eficiência do programa.   

# ele é igual uma expressão geradora, a diferença está na sintaxe e na complexidade do que está sendo gerado. uma função geradora é definida usando a palavra-chave def e pode conter múltiplas instruções yield, enquanto uma expressão geradora é definida usando uma sintaxe de compreensão de lista ou tupla e geralmente é usada para gerar uma sequência de valores simples.

# exemplo de expressão geradora para lembrar a diferença:   
contador = (x for x in range(0, 4)) 

print(next(contador))  # Imprime 0             
print(next(contador))  # Imprime 1
print(next(contador))  # Imprime 2
print(next(contador))  # Imprime 3
#print(next(contador))  # Levanta StopIteration  
