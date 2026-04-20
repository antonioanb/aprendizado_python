""" O Closure ocorre quando uma função interna referencia variáveis de uma função externa, e a função externa retorna essa função interna. Isso permite que a função interna "capture" e preserve o estado (os dados) do momento em que foi criada.
"""
def fazer_saudacao(msg):
    # Esta função interna "lembra" do escopo da função externa
    def saudar(nome):
        # msg não foi definida aqui, mas 'saudar' mantém o acesso a ela
        return f"{msg} {nome}"
    
    # Closure: retornamos a função interna sem executá-la (sem os parênteses)
    # Ela leva consigo o "ambiente" onde foi criada (o valor de msg)
    return saudar

# Cada variável abaixo é uma instância diferente da função 'saudar'
# falar_bom_dia "salvou" a msg "Bom Dia" na memória
falar_bom_dia = fazer_saudacao("Bom Dia")
# falar_boa_noite "salvou" a msg "Boa Noite"
falar_boa_noite = fazer_saudacao("Boa Noite")

# Mesmo que 'fazer_saudacao' já tenha terminado de executar, 
# as funções abaixo ainda sabem o valor de 'msg'.
print(falar_bom_dia("Eduardo"))
print(falar_boa_noite("Antonio"))

# ---
nomes = ["rodrigo", "marcia", "cintia", "mario"]

for nome in nomes:
    # Reutilizando a lógica customizada salva no closure
    print(f"{falar_bom_dia(nome)} 😄")
    print(f"{falar_boa_noite(nome)} 😴")