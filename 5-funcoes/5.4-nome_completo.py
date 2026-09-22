# Criando a função nome completo
def nome_completo(nome,sobrenome):
    return f"{nome} {sobrenome}"

# Solicitando os dados do usuário
nome_usuario = input("Digite seu nome: ")
sobrenome_usuario = input("Digite seu sobrenome: ")

# Chamando a função e criando o nome inteiro
nome_inteiro = nome_completo(nome_usuario,sobrenome_usuario)

# Apresentando uma mensagem de boas vindas ao usuário
print(f"Bem-vindo(a), {nome_inteiro}")