# Take two coma separated inputs from user
# 1. user's name
# 2. a single charachter

# output - 2 print lines 
# 1. user's name length
# 2. count the charachter that user inputed

name,char = input('Enter your name: ').split(',')
# name.lower().count(char.lower())
# char.lower()
print(f"Your Name is {name} and length of characters are : {len(name)} ")
print(f"Character count: {name.count(char)}")
print(f'Character count is: {name.lower().count(char.lower())}')

