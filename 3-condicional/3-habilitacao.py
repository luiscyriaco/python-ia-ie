#  Solicitando o nome e a idade do usuário
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

# Criando a condição caso for >= a 18anos
if idade >= 18:
    print("Maior de Idade")
else:
   print("Menor de Idade")