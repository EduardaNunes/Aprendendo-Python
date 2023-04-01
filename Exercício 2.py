votos = [];
x = 1;
candidatoAnterior = '';
contador = 0;

while True:
    print('Vote em um candidato! (vote de 0 a 9):');
    voto = input();
    
    if voto == '' and len(votos) != 0:
        votos.sort()
        votos.append('FIM')

        for i in votos: 
            contador += 1;

            if contador != 1:
                if i == candidatoAnterior:
                    x += 1

                else:
                    print('Candidato '+str(candidatoAnterior)+ ' obteve ' + str(x) + ' votos')
                    x=1

            candidatoAnterior = i;

        break
    elif voto == '' and len(votos) == 0:
        print('Não Houve Nenhum Voto')
        break
    elif voto.isnumeric() == False:
        print('Esse voto não corresponde a nenhum candidato')
        break

    votos.append(int(voto))