# fromkeys() method

d = {'name': 'Unknown', 'age': 'unknown'}
print('===================================================')

d = dict.fromkeys(['name', 'age','height'], 'unknown')
print(d)
print('===================================================')

# get() method 
pop = dict(name='bob smith',age=42,pay='10000',job='dev')
print('===================================================')

# print(pop)
print(pop['name'])
print('===================================================')

print(pop.get('pay'))  # Use of get method
print('===================================================')

print('===================================================')
# use of clear method
d.clear()
print(d)

print('===================================================')
# use of copy method
pop_pop = pop.copy()
print(pop_pop)