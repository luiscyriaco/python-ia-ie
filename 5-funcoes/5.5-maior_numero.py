# criando função maior_numero
def maior_numero(x,y):
    if x > y:
        return x
    else:
        return y

# solicitando os 2 números ao usuário
numero_1 =  float(input("Digite um número: "))
numero_2 =  float(input("Digite outro número: "))

# chamando a função que verifica o maior número
resultado = maior_numero(numero_1,numero_2)

# apresentando o maior número ao usuário
print(f"O maior número digitado foi: {resultado}")


