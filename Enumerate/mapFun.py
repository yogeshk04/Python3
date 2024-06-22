# map function

numbers = [1,2,3,4,5,6,7]

def square(a):
    return a**2

squares = list(map(square, numbers))

print(squares)

print('===================== using Labmda ========================')
squares = list(map(lambda a:a**2, numbers))
print(squares)

print('===================== list comprehension ========================')
sqr = [i**2 for i in numbers]
print(sqr)

