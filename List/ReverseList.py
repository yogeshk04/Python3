# Defice a function which will return a reverse of list.

def revList(inList):
    inList.reverse()
    return inList


lst = [1,2,3,4,5,6,7,8,8]
print(f'List is: {lst}')
print(f'Reversed list is: {revList(lst)}')


lst1 = [11,22,33,44,55]

def rev_List1(lstToRev):
    return lstToRev[::-1]

print(rev_List1(lst1))


def reverse_list(ls):
    rev_list = []
    for i in range(len(ls)):
        pop_item = ls.pop()
        rev_list.append(pop_item)
    return rev_list

co_list = [6,7,8,9,8,0,2]
print(f'Reverse List using POP function is: {reverse_list(co_list)}')