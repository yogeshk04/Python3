def fun1(lst, **kwargs):
    if kwargs.get('reverse_srt') == True:
        return [name[::-1].title() for name in lst]
    else:
        return [name.title() for name in lst]

    
names = ['yogesh', 'nikam']
print(fun1(names))

print(fun1(names, reverse_srt = True))