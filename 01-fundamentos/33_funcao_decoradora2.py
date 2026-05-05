
def decoradora(func):

    def interna(*args):
        #valida os parametros antes de chamar a função original.
        checar_parametros(args)
        resultado = func(*args)
        return resultado
    return interna

#aplica o decorador de forma automatica usando a sintaxe @decoradora. Isso é equivalente a inverter_string = decoradora(inverter_string), mas é mais conciso e legível.
@decoradora
def inverter_string(string):
    return string[::-1]

def checar_parametros(params):
    for param in params:
        if not isinstance(param, str):
            raise ValueError("O parametro deve ser uma string") 

#quando inverter_string("Python") é chamada, a função decoradora é executada, verificando se o parametro é uma string, e em seguida chamando a função inverter_string para inverter a string "Python".
invertida = inverter_string("Python")
print(invertida)  # Imprime "nohtyP"