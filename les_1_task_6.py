"""
6. По длинам трех отрезков, введенных пользователем, определить возможность
 существования треугольника, составленного из этих отрезков. Если такой треугольник существует,
 то определить, является ли он разносторонним, равнобедренным или равносторонним.

"""

a=int(input('Введите длину отрезка 1: '))
b=int(input('Введите длину отрезка 2: '))
c=int(input('Введите длину отрезка 3: '))

if a+b>c and b+c>a and a+c>b:
    print('Треугольник существует')
    if a!=b and b!=c and a!=c:
        print('Он разносторонний')
    elif (a==b or b==c or a==c) :
        print('Он равнобедренный')
    elif a==b and b==c and a==c:
        print('Он равносторонний')
else:
    print('Треугольника не существует')