
lst = ['abc', 'lmn', 'xyz']

print('=======================================')
lc = [lc1[::-1] for lc1 in lst]
print(lc)

print('=======================================')
# using fuction
def lc_rev(lis):
    return [lc[::1] for lc in lis]

print(lc_rev(lc))

print('=======================================')

def num_seperator(l):
    even_n = []
    odd_n = []
    for i in l:
        if i % 2 == 0:
            even_n.append(i)            
        else:
            odd_n.append(i)
    # print(f'Even numbers: ' % even_n)
    # print(f'Odd number: ' % odd_n)
    return even_n,odd_n

print('=======================================')
r_lst = list(range(1,21))
# print(r_lst)
print(num_seperator(r_lst))

print('=======================================')
# using list comprehension
even_numbers = [i for i in r_lst if i%2 ==0]
print(type(even_numbers))
print(f'Even number list: ' + str(even_numbers))

# or 

print(f'Even number list: ' + str([i for i in r_lst if i%2 ==0]))
print('=======================================')

odd_numbers = [i for i in r_lst if i%2 != 0]
print(f'Odd number list: ' + str(odd_numbers))