'''
write a python program to read pasword as input from the user and check weather it is valid pasword or invalid pasword
'''

s=input("ENTER YOUR PASWORD: ")
upper=0
lower=0
special=0
for i in s:
    if i.isalpha() and i.isupper():
        upper+=1
    elif i.isalpha() and i.islower():
        lower+=1
    else:
        special+=1
if (upper>=1 and lower>=1 and special>=1):
    print("VALID PASSWORD")
else:
    print("INVALID PASSWORD")


