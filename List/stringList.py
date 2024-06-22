
# write a function which return reverse of list as ['cba','fed','zyx']

def str_ls_rev(ls):
    rev_lst = []
    for i in ls:
        rev_lst.append(i[::-1])
    return rev_lst

str_list = ['abc','def','xyz']

print(str_ls_rev(str_list))
