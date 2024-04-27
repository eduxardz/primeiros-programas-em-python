import math
ang = float(input("Digite um angulo"))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
print("O sen é {:.2f}, o cos é {:.2f} e a tangente é {:.2f}".format(sen, cos, tg))