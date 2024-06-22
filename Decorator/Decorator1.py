
def sqr(a):
    return a*a

st = sqr

print(st.__name__)
print(sqr.__name__)

print(st(9))

print(sqr)
print(st)