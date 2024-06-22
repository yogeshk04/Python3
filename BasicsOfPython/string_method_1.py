# replace() method
# find() method

strng = 'We are developing MindSphere Application, There are many other application'

print(strng.replace('are', 'is'))

is_pos1 = strng.find('is')
is_pos2 = strng.find('is', is_pos1)

print(is_pos2)