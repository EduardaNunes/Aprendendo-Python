fim = 'fim'
numeros = []

print ('Escreva um número inteiro ou digite fim para terminar:')
x = input()
teste = x.isnumeric()

while teste == True: 

    numeros.append(int(x))
    print ('Escreva um número ou digite fim para terminar:')
    x = input()
    teste = x.isnumeric()

if x == fim:
    
    numeros.sort()
    y = len(numeros)
    soma = sum(numeros)
    media = soma / (y+1)

    print ('Menor: ' + str(numeros[0]) + '  |  Maior: ' + str(numeros[y-1]) + '  |  Média: ' + str(media))

else: 
    print('ERROR - Por favor insira um número válido')



