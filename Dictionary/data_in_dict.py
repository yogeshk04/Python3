# Take a input from user and store it into dictionary

# empty dictionary
user_input = {}

name = input('Enter your name: ')
age = input('Enter your age: ')
friends = input('Enter your friend \'s name seperated by comma: ').split(',')

user_input['name'] = name
user_input['age'] = age
user_input['friends'] = friends

print(user_input)

print('===================================================')

for i, j in user_input.items():
    print(i,j)