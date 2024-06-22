# add the user input number digit

num = input('Enter the multidigit number: ')
sum =0
i = 0

print(len(num))
print(num[0])
print(num[1])
print(num[2])
print(num[3])

while i < len(num):
    sum+=int(num[i])

    i += 1
print(f'Sum is: {sum}')
