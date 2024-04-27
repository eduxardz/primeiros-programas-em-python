dist = float(input("Digite a distância pecorrida em Km: "))
km1 = (dist*0.45)
km2 = (dist*0.5)
if dist > 200:
    print('Esse será o valor cobrado: {}'.format(km1))
else:
    print('Esse será o valor cobrado: {}'.format(km2))