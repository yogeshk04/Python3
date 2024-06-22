

sqr = []
for i in range(1,11):
    sqr.append(i**3)
print(sqr)

print('=======================================')
# Using list comprehension

sqr = [i**2 for i in range(1,21)]
print(sqr)

print('=======================================')
neg_num = []

for i in range(1,11):
    neg_num.append(-i)
print(neg_num)

print('=======================================')
# Using list comprehension
neg_num_1 = [-i for i in range(1,21)]
print(neg_num_1)

print('=======================================')
