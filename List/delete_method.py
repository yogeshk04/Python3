# Deletin last element using pop method

print('********************** New **********************')
color = ["Green", 'Blue','Red','Orange','Black','Red']
print(color)
color.pop()
print(color)
color.pop(2)
print(color)

# delete operator
print('********************** New **********************')
del color[3]
print(color)

# remove() method
print('********************** New **********************')
color.remove('Green')
print(color)
# color.remove('Green1')
print(color)

# remove method for multiple values in list
print('********************** New **********************')
col = ["Green", 'Blue','Red','Orange','Black','Blue','Red','Blue']
col.remove('Blue')
print(col)

# Check if the element in the list
print('********************** New **********************')
if 'Blue' in col:
    print('Blue is there in the list')
else:
    print('Blude is not there in the list')