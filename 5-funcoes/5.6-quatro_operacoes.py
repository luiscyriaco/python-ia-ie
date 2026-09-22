from funcoes_operacoes import somar,subtrair,multiplicar,dividir

numero_1 = float(input("Digite um número: "))
numero_2 = float(input("Digite outro número: "))

resultado_soma = somar(numero_1, numero_2)
print(f"Soma: {resultado_soma}")
print(f"Subtração: {subtrair(numero_1,numero_2)}")
print(f"Multiplicação: {multiplicar(numero_1,numero_2)}")
print(f"Divisão: {dividir(numero_1,numero_2)}")