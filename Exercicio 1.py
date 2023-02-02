def repeat ():
    print ('Gostaria de Começar Denovo? S/N ')
    resposta = input();

    if resposta == 'S':
        main()
    elif resposta =='N':
        print('Programa Finalizado')
    else:
        print('Resposta Inválida')
        repeat()

def main():

    numeros = []
    teste = True
    x = 0

    while teste == True: 

        numeros.append(int(x))
        print ('Escreva um número ou digite fim para terminar:')
        x = input()
        teste = x.isnumeric()

    if x == 'fim':
        
        numeros.pop(0)
        numeros.sort()
        y = len(numeros)
        soma = sum(numeros)

        if y == 0 :
            print('Por Favor Insira Algum Número Para Ser Calculado')
            main()

        media = soma / y

        print ('Menor: ' + str(numeros[0]) + '  |  Maior: ' + str(numeros[y-1]) + '  |  Média: ' + str(media))
        repeat()

    else: 
        print('ERROR - Por favor insira um número válido')
        main()

main()