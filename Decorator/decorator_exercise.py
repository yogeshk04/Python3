# only int allow

from functools import wraps


def only_int_allow(fun):
    @wraps(fun)
    def wrapper (*args, **kwargs):
        data_types = []
        for arg in args:
            data_types.append(type(arg)==int)
        if all(data_types):
            return fun(*args, **kwargs)
        else:
            print("Invalid input parameter")
    return wrapper


@only_int_allow
def add_all(*args):
    total = 0
    for i in args:
        total += i
    return total

print(add_all(1,2,3,4,5,6,7,8,9,10))
print("------------------------------------------------------------")
print(add_all(1,2,3,4,5,6, 'yo'))
