name = 'Chiu'
age = 2

if name == 'Chiu' and age == 2:
    print('True')
else:
    print("False")


# if_elif_else
age = int(input('Enter your age: '))

if 0<age<=18:
    print('You are a child')
elif 18>age<=45:
    print('You are an adult')
elif 45>=age<=60:
    print('YOur are old')
else:
    print('Your are very old')