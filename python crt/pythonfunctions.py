'''
write a python programe to read a string as input from the user and print 
1.count of uppercase
2.count of lowercase
3.count of numeric values
4.count of special characters
'''


s=input("ENTER THE STRING: ")
uppercase =0
lowercase=0
numeric=0
special=0
for i in s:
    if i.isupper():
        uppercase+=1
    elif i.islower():
        lowercase+=1
    elif i.isdigit():
        numeric+=1
    else:
        special+=1
print(f"COUNT OF UPPERCASES LETTERS IN {s} is {uppercase}")
print(f"COUNT OF LOWERCASES LETTERS  IN {s} is {lowercase}")
print(f"COUNT OF NUMERIC DIGITS IN {s} is {numeric}")
print(f"COUNT OF SPECIAL CHARACTERS IN {s} is {special}")



