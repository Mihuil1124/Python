#Phyton 3.8.0 File

a = int (input('Введи первое число- '))
b = int (input('Введи второе число- '))
z = int (input('Введи номер операции \n 1 Сложение \n 2 Вычитание \n 3 Умножение \n 4 Деление \n'))

if z == 1:
    q = a + b

if z == 2:
    q = a - b

if z == 3:
    q = a * b

if z == 4:
    q = float(a / b)

print (q)
