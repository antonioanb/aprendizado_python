"""
CONCEITO: Operadores Lógicos (and, or, not)
Usados para combinar múltiplas condições em uma única expressão.
"""

# ---------------------------------------------------------
# 1. AND (E): Exige 100% de verdade.
# Regra: Só resulta em True se TODAS as condições forem True.
# ---------------------------------------------------------
ingresso = True
documento = True

if ingresso and documento:
    print("Entrada permitida 🍿")

# ---------------------------------------------------------
# 2. OR (OU): Exige o mínimo de verdade.
# Regra: Resulta em True se PELO MENOS UMA for True.
# ---------------------------------------------------------
estudante = False
idoso = True

if estudante or idoso:
    print("Desconto aplicado 💸")

# ---------------------------------------------------------
# 3. NOT (NÃO): O Inversor.
# Regra: Inverte o estado booleano (True -> False / False -> True).
# ---------------------------------------------------------
chovendo = False

if not chovendo:
    print("Indo treinar 💪")

# ---------------------------------------------------------
# 4. COMBINAÇÕES E PRECEDÊNCIA
# Regra: Parênteses () definem o que deve ser resolvido primeiro.
# ---------------------------------------------------------
tem_dinheiro = True
feriado = False
fds = True

# Se tem dinheiro E (é feriado OU fim de semana)
if tem_dinheiro and (feriado or fds):
    print("Partiu viagem! ✈️")

"""
RESUMO DA TABELA VERDADE:
| Operador | Regra Prática                      |
|----------|------------------------------------|
| AND      | Tudo tem que ser verdade           |
| OR       | Um "sim" já basta                  |
| NOT      | Do contra (inverte tudo)           |
"""