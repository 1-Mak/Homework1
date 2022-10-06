katet1 = int(input('Введите значение катета (число): '))
katet2 = int(input('Введите значение другого катета (число): '))
hypotenuse = (katet1**2+katet2**2)**0.5
S = ((katet1*katet2)/2)
P = (katet1 + katet2 + hypotenuse)
print('Площадь = ',S,'Периметр = ',"{:7.3f}".format(P))