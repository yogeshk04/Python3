
def odd_even_filter(ls):
    odd_num = []
    even_num = []
    for i in ls:
        if i % 2 != 0:
            odd_num.append(i)
        else:
            even_num.append(i)
    comb_list = [even_num,odd_num]
    return comb_list

lst = range(1,21)

print(odd_even_filter(lst))