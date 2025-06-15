'''
write a python program to print uppercase alphabets from a to z inclusing thier asci values

for i in range(27):
    print(chr(i+65),f"-------->{i+65}")
for i in range(27):
    print(chr(i+96),f"-------->{i+96}")
    '''

'''
    write a python prgrame to read a input from user and print its asci value

s=input("ENTER THE CHARACTER:")
print(ord(s))
'''
#write a python program to read a string as input from the user and replace all vowels with 0
s=input("ENTER THE STRING: ")
for i in s:
    if i in 'aeiouAEIOU':
        s=s.replace(i,'0')
print(s)

            

     