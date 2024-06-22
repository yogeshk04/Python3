bob=dict(name='bob smith',age=42,pay='10000',job='dev')
print('===================================================')
# if key present in dictionary
if 'name' in bob:
    print('Yes')
else:
    print('No')

print('===================================================')
# if vale present in dict
if 42 in bob.values():
    print('Yes')    
else:
    print('No')

print('===================================================')
#  For loop in dictionary.
# printing keys
for i in bob:
    print(i)
print('===================================================')
# printing values 
for i in bob.values():
    print(i)
print('===================================================')

