import random
al = str(input('Digite o nome do líder do grupo: '))
al1 = str(input('Digite o nome do líder do grupo: '))
al2 = str(input('Digite o nome do líder do grupo: '))
al3 = str(input('Digite o nome do líder do grupo:'))
lista_ap = [al, al1, al2, al3]
random.shuffle(lista_ap)
print('O resultado foi: {}'.format(lista_ap))
