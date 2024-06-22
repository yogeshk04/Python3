# Python uses C-style string formatting to create new, formatted strings.
# The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list),
# together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s" and "%d".

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
print("Students Name: %s" % list(Dict.items()))