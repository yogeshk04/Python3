# Docorators: enhance the functionnality of other functions

def func1():
    print("This is function 1")

def func2():
    print("This is function 2")


# enhance the function 1 and 2
# Here comes the decorator function in picture:

def dec_fun(anyFunc):
    def wrapp_func():
        print("***** Line to enhance the existing function *****")
        anyFunc()
    return wrapp_func

func1 = dec_fun(func1)
func1()

print("---------------------------------------------")

func2 = dec_fun(func2)
func2()

print("======================================================================")
@dec_fun
def funct1():
    print("Using decorator short cut for function 1")
funct1()
print("---------------------------------------------")

@dec_fun
def funct2():
    print("Using decorator short cut for function 2")
funct2()