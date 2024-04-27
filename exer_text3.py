name = (input('Digite seu nome completo: '))
nam = name.split()
print('Seu primeiro nome é: {}'.format(nam[0]))
print('Seu último nome é: {}'.format(nam[len(nam) - 1]))

'''
A função 'len' mede o comprimento dafrase fatiada ou seja se o nome digitado foi
Giovanni Manganotti Machado, a função split vai dividir o nome em blocos

[Giovanni], [Manganotti], [Machado] , porem a função len começa a contar apartir do numero 1
mas as posições na lista começam a contar apartir do 0, entao para nao dar erro e você conseguir
pegar a ultima posição é necessario fazer o tamanho da frase - 1

Representação:

Nome Digitado:   Giovanni   Manganotti      Machado 
                    0            1             2

Função len(do nome fatiado)

           [Giovanni], [Manganotti], [Machado]
                1           2           3

Como é visto no esquema acima a contagem  na lista começa apartir do numero 1
logo é necessario tirar um da lista para chegar ao ultimo nome                      
'''