# Exercise to find out the cube in dictionary

def cube(n):
    cubes = {}
    for i in range(1, n+1):
        cubes[i] = i**3
    return cubes

# print('Dict: ' % cube(20))
print(cube(10))