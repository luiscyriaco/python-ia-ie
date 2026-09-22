# Solicitando os dados do paciente
nome = input("Digite o nome do paciente: ")
peso = float(input("Digite o peso do paciente Kg: "))
altura = float(input("Digite a altura do paciente m: "))

# Calculando o IMC do paciente
imc = peso / altura ** 2

# Definindo o quadro do paciente segundo o IMC
if imc < 18.5:
    situacao = "Abaixo Peso"
elif imc <= 24.9:
    situacao = "Peso Normal"
elif imc <= 29.9:
    situacao = "Sobrepeso"
elif imc <= 34.9:
    situacao = "Obesidade grau I"
elif imc <= 39.9:
    situacao = "Obesidade grau II"
else:
    situacao = "Obesidade grau III"

print(f"O IMC do paciente {nome} é {imc} e ele(a) está {situacao}")
