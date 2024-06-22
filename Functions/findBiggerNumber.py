# Function to find out the bigger numbe of two   

def comp(n1, n2):
    if n1 > n2:
        print(f'Bigger number is {n1} ')
    print(f'Bigger number is {n2} ')

# Take a user input for two numbers
# num1 = int(input('Enter the first number: '))
# num2 = int(input('Enter the second number: '))

# call the comparison Function
# comp(num1,num2)


def biggerNum(a,b,c):
    big = comp(a,b)
    return comp(big,c)

print(biggerNum(2,3,4))
