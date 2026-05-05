#decorador é um padrão de projeto que ultiliza Closures para modificar ou extender o comportamento de uma função sem alterar seu codigo fonte.

#padrão de projeto é uma solução estabelicido para um problema comum em desenvolvimento de software. 

#função decoradora.
def decoradora(funcao):

    def interna(*args):
        for arg in args:
            checar_param(arg)
        resultado = funcao(*args)
        return resultado
    return interna

#função decorada, que é a função inverter_string decorada com a função decoradora.
def inverter_string(string):
    return string[::-1]

#função para checar se o parametro é uma string, caso contrário levanta um erro.
def checar_param(param):
   if not isinstance(param, str):
        raise ValueError("O parametro deve ser uma string") 
   
#criando a função decorada, passando a função inverter_string como argumento para a função decoradora. Isso cria uma nova função chamada criar_inverter_string, que é a versão decorada da função inverter_string.
criar_inverter_string = decoradora(inverter_string)

#quando criar_inverter_string("Python") é chamada, a função decoradora é executada, verificando se o parametro é uma string e, em seguida, chamando a função inverter_string para inverter a string "Python". O resultado é armazenado na variável invertida e impresso na tela.    
invertida = criar_inverter_string("Python")
print(invertida)  # Imprime "nohtyP"
