information = [{'nome': 'Vitor', 'idade': '18', 'cidade': 'Osasco'},
               {'nome': 'Vitória', 'idade': '18', 'cidade': 'Osasco'}
               ]

information[1]['idade'] = 19
information[0]['profissão'] = 'Punheteiro'
information[1]['cidade'] = 'Campinas'
del information[0]['idade']

print(information)


# ===== 3- Dicionário com números e seus quadrados (1 a 5) ====


quadrados = {x: x**2 for x in range(1, 6)}
print(quadrados)

# ==== 4 - Verificar se uma chave existe em um dicionário ====

information = [{'nome': 'Vitor', 'idade': '18', 'cidade': 'Osasco'}]

if 'idade' in information:
    print("A chave 'Idade' existe")
else:
    print("Chave 'Idade' não encontrada!")


# ==== 5 - Contar frequência de palavras em uma frase ====

frase = "o rato roeu a roupa do rei de roma"
palavras = frase.split()
frequencia = {}

for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1

print(frequencia)
