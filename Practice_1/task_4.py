""" 
Процентная ставка по вкладу.
Порядок ввода входных данных:
1.Процентная ставка
2.Рублевая часть вклада
3.Копеечная часть вклада
"""

p= int(input())
x= int(input())
y= int(input())
rub=int()
cop=int()
stsum=str(round((x*100+y)*(100+p)/100))
cop=stsum[len(stsum)-2:]
rub=stsum[:len(stsum)-2]
print(rub)
print(cop)