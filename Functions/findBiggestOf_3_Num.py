# take a user input for three numbe and find the bigest one.

def biggest_Of_3(a, b, c):
    if a > b and a > c:
        return print(f'Biggest of three is a: {a}')
    elif b > a and b > c:
        return print(f'Biggest of three is b: {b}')
    else:
        return print(f'Biggest of three is c: {c}')

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))

biggest_Of_3(n1,n2,n3)