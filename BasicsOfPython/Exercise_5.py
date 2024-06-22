# Gaming exercise

w_num = 44
g_num = int(input("Enter nubmer between 0 to 100 : "))

if w_num == g_num:
    print("Congratulation, You Won!")

else:
    if g_num < w_num:
        print('Too low')
    else:
        print('Too high')
    