# Solicitando nome e notas do aluno
nome = input("Digite seu nome: ")
nota_1 = float(input("Digite primeira nota: "))
nota_2 = float(input("Digite segunda nota: "))
nota_3 = float(input("Digite terceira nota: "))

# Realizando o cálculo da média
media = (nota_1 + nota_2 + nota_3 ) / 3


if media < 4:
    situacao = "Reprovado"
elif media <= 6:
    situacao = "Recuperação"
else:
    situacao = "Aprovado"

print("A média do aluno(a) ",nome, " é ", media, " ele foi ", situacao)
print(f"A média do aluno(a) {nome} é {media:.2f} ele foi {situacao}")
