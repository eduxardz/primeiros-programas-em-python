import random
num1 = str(input('Digite o nome de um aluno:'))
num2 = str(input('Digite o nome de um aluno:'))
num3 = str(input('Digite o nome de um aluno:'))
num4 = str(input('Digite o nome de um aluno:'))
lista = (num1, num2, num3, num4)
escolhido = random.choice(lista)
print('O aluno escolhido para ganhar o kit foi: {}'.format(escolhido))