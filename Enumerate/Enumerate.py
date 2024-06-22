# we use enumerate function with for loop to track position of our item in iterable

colors = ['red', 'yellow','white','blue']

position = 0
for col in colors:
    print(f"{position} ---> {col}")
    position +=1


print("============================")
# using enumerate function

for position, color in enumerate(colors):
    print(f'{position}-->{color}')

print("============================")
# Function to find out the position of a string from a list
def postFinder(lst, target):
    for p, color in enumerate(lst):
        if color == target:
            return p
    return -1

print("============calling the function================")
print(postFinder(colors, 'white'))
print(postFinder(colors, 'blue'))
print(postFinder(colors, 'Green'))
