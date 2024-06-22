# Ask your's name and age
# If user's name and age start wit h( a or A) and age is about 10 then print your can watch movie
# Else sorry, you cannot.
user_name = input("Enter you name: ")
user_age = int(input("Enter your age: "))

print(f'Hello {user_name}, your age is {user_age}')

if (user_name[0] == 'a' or user_name[0]== 'A') and user_age > 10:
    print('You can watch movie')
else:
    print("Sorry you can't.")