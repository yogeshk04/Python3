name = input('Enter you name: ') 

temp = ""
i = 0

while i < len(name):
    if name[i] not in temp:
        temp += name[i]
        print(f'{name[i]} : {name.count(name[i])}')
    i += 1
    