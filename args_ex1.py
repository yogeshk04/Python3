def power(num, *args):
    if args:
        return [i**num for i in args]
    else:
        return "Didn't pass anything"

nums = [1,2,3,4]
print(power(3, *nums))