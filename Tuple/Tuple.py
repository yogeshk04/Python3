# A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. 
# The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, 
# whereas lists use square brackets. Creating a tuple is as simple as putting different comma-separated values.

tuple_ex = ('Green', 'Yellow', 'Red','Black')

print(tuple_ex)

# You will get an error: TypeError: 'tuple' object does not support item assignment
# tuple_ex[1] = 'Pink'

print(type(tuple_ex))

num = '1', '2' , 'numbers'
print(type(num))

print(num)