altura = float(input("Digite sua altura: "))
idade = int(input("Digite sua idade: "))

permissao = (altura >= 1.40) and (idade >= 12)

print("Permissão para andar na montanha-russa: ", permissao)