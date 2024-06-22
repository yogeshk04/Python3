# define a function take any no of lists containingnumbers
# [1,2,3], [4,5,6], [7,8,9]
# and return average 
# (1+4+7)/3, (2+5+8)/3, (3+6+9)/3

def avg_finder(*args):
    average = []
    for pair in zip(*args):
        average.append(sum(pair)//len(pair))
    return average

print(avg_finder([1,2,3], [4,5,6], [7,8,9]))

print("==============================================")
av_finder = lambda *args: [sum(pair)/len(pair) for pair in zip(*args)]

print(av_finder([1,2,3], [4,5,6], [7,8,9]))