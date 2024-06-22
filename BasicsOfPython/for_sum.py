# sum of numbers 

num = int(input('Enter the number: '))
total = 0

for num in range(1,num+1):
    total +=num
    print(f'Your value: {num}')
print(f'Sum is: {total}')

