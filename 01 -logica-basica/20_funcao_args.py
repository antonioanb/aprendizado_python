def soma(*args):
    #args é uma tupla, ele empacota os valores recebidos
    total = 0 
    for numero in args:
        total += numero
    return total

somar = soma(20,50,60,80)#é possivel passar quantos argumentos não nomeados quiser

numeros = 30, 60, 50, 40 ,80#tupla de numeros

somar2 = soma(*numeros)#passando uma tupla como argumento, desempacotando ele pra isso pois a função não espera uma tupla 

print(somar)
print(somar2)