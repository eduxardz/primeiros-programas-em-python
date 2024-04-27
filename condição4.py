year = int(input('Digite um ano secular: '))
bisx = (year%4 == 0)
if year == bisx:
    print('É um ano bisexto!!')
    if bisx%400 == 0:
        print('É um ano bisexto!!')
        if bisx //: