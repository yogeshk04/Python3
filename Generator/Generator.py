# creating generator

# using generator function

def nums(n):
    for i in range(1,n+1):
        # print(i)
        yield (i) # yield is a keyword so you don't have to write i in perenthesis because it's not a function, you can write 'yield i'


print(nums(10))