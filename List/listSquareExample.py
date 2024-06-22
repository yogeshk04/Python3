# Define a function which will take a list as input and return square of all values from list.


def squareList(lstInput):
    lst = []
    for i in lstInput:
        lst.append(i**2)
    return lst

NumList = [1,2,3,4,5]
print(squareList(NumList))

print("========================= New =========================")
oneList = list(range(1,11))
print(f"List created by range function: {oneList}")
print(f'Square of list is: {squareList(oneList)}')