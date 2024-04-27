capital = int(input('Digite o valor do Financiamento: '))
parc = int(input('Digite o número de parcelas: '))
juros = float(input('Digite a taxa de juros a ser cobrado pela Instituição: '))
amort = capital / parc
jur = capital * (juros/100)
dimin = amort * (juros/100)
mes1 = amort + jur
prox_parc = (amort - dimin) + jur
ult = amort + dimin

print('A primeira parcela é {} e a ultima parcela é {}'.format(mes1, ult))

parcelas = [mes1]

for i in range(1, parc):
    prox_parc = (amort - dimin) + jur
    parcelas.append(prox_parc)
    amort -= dimin

print("\033[4;30;44mParcelas:\033[m", parcelas)