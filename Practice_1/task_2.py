""" 
Задача про МКАД
Порядок ввода входных данных:
1. Скорость
2. Время
"""

v = int(input())
t = int(input())
a=divmod(abs(t*v)+109,109)
chast=a[0]-1
sm=abs(t*v)-chast*109
if t*v<0:
    p=109-sm
else:
    p=sm
print(p)