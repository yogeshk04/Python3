# This program explains about *args

def total(*args):
    num = 0
    for i in args:
        num += i
    return num

print(total(1,2,3,4,5))
print(total(1,2,3,4,56,78,90,9,87,65,4,3))

