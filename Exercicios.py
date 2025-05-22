#  === Exercicio 1 ===

numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = ['Vitor', 'Gabriel', 'Vitória', 'Mathias']
ano_nascimento = [2006, 2025]
soma = 0
impar = 0

#  === Exercicio 2 ===

for num in numero:
    if num % 2 != 0:
        impar += 1
        print(num, end = ' ')
        soma += num

#  === Exercicio 3 ===

print(f"\nA soma dos números impares é de: {soma}\n")

#  === Exercicio 4 ===

for i in range(10, 0,-1):
    print(i, end = '  ')

#  === Exercicio 5 ===

num = int(input("\nDigite um número para ver a tabuada dele: "))

for i in range(0,10):
    print(f"\n{num} * {i} = {num * i}")

#  === Exercicio 6 ===


numeros = [1, 10, 12, 16, 53, 76, None, 32, 12]

soma = 0

for num in numeros:

    try:     
        soma += num


    except:
         print(f"Valor inválido ignorado: {num}")

print(f"\nSoma total: {soma}")

#  === Exercicio 7 ===


lista = [1, 10, 12, 16, 53, 76, 32, 12]
soma = 0


for num in lista:
    soma += num

try:
    media = soma / len(lista)
    print(f"A média dos valores é: {media}")

except ZeroDivisionError:
    print("Não é possivel calcular a média de uma lista vazia!")

