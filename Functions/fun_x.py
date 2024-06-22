def comp(a, b):
    if a > b:
        return a
    return b

print(comp(2,3))

print('************************ New function ************************')

def greaterNum(a, b, c):
    # c1 = comp(a,b)
    # return comp(c1,c)
    return comp(comp(a,b), c)

print(greaterNum(2,4,6))