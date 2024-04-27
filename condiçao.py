import random
number = int(input('Digite um número: '))
list = [0, 1, 2, 3, 4, 5]
num = random.choice(list)
if number > num:
    print("Você perdeu!")
else:
    print('Você Ganhou!!!')
print('O número escolhido pela máquina foi {}'.format(num))

