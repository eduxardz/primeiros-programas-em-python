velocidade = int(input('Digite a velocidade a qual o veículo estava: '))
km = (velocidade - 80)*80
if velocidade > 80:
    print('O propriétario deste veículo será multado em: R${}'.format(km))
else:
    print('De acordo com os dados informados o proprietário do veículo não pagará nenhuma multa!')