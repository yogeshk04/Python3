# keyword arguments kwargs (**kwargs)

def funct(name, **kwargs):
    for i, j in kwargs.items():
        print(f'{i}:{j}')
    
funct('Manu', f_name = 'Yogesh', l_name = 'Nikam')

# order of arguments in a function

def function1(name, *args, last_name='Unkown',**kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

function1('yogesh', 1,2,3,4,5, 'nikam', fruit = 'mango', color = 'Red')