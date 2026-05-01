dados_variados = [1, 2.5, "Python", [1, 2, 3], {"chave": "valor"}, (4, 5), {1, 2, 3}, None]


# a função isinstance() é usada para verificar se um objeto é uma instância de um tipo específico ou de uma classe. Ela retorna True se o objeto for do tipo especificado ou de uma subclasse, e False caso contrário.
for item in dados_variados:
    if isinstance(item, int):
        print(f"{item} é um inteiro.")
    elif isinstance(item, float):
        print(f"{item} é um número de ponto flutuante.")
    elif isinstance(item, str):
        print(f'"{item}" é uma string.')
    elif isinstance(item, list):
        print(f"{item} é uma lista.")
    elif isinstance(item, dict):
        print(f"{item} é um dicionário.")
    elif isinstance(item, tuple):
        print(f"{item} é uma tupla.")
    elif isinstance(item, set):
        print(f"{item} é um conjunto.")
    else:
        print(f"{item} é de um tipo desconhecido.")
