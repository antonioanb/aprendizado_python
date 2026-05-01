"""
DICIONÁRIOS (dict)
Estruturas de dados que armazenam pares de 'chave: valor'.
Chaves são únicas e funcionam como o índice personalizado do dado.
"""

# ---------------------------------------------------------
# 1. CRIAÇÃO E ESTRUTURA
# ---------------------------------------------------------
pessoa = {
    'nome': 'Antonio',
    'sobrenome': 'Barros',
    'idade': 36,  # Note: melhor usar int para idade
    'enderecos': [
        {'rua': 'Vitoria', 'numero': 110},
        {'rua': 'Silva', 'numero': 230},
    ]
}

# ---------------------------------------------------------
# 2. MANIPULAÇÃO (CRUD de Chaves)
# ---------------------------------------------------------
# Criar ou Atualizar
pessoa['cidade'] = 'Belford Roxo' 

# Acessar com segurança (O método .get evita erros se a chave não existir)
profissao = pessoa.get('profissao', 'Não informada')

# Deletar
if 'cidade' in pessoa:
    del pessoa['cidade']

# ---------------------------------------------------------
# 3. CHAVES DINÂMICAS
# ---------------------------------------------------------
# Muito útil quando o nome da chave vem de uma variável ou input
campo_novo = 'tecnologia_foco'
pessoa[campo_novo] = 'Python'