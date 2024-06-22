# lambda expression

# nofmal function
def if_even(a):
    if a % 2 == 0:
        return True
    return False
print(if_even(2))

isEvern = lambda a: a% 2 == 0

print(isEvern(5))

# lambda if else example
def funk(s):
    if len(s) > 5:
        return True
    return False

def funk1(s):
    return len(s) < 5

print(funk('yogesh'))
print(funk1('yogesh'))

f1 = lambda s : True if len(s) > 5 else False

f = lambda s : True if len(s) > 4 else False

print(f('Yog'))

