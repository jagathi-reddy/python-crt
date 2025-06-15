n=int(input("ENTER A NUMBER: "))
if(n>=-9 and n<=9):
    print(f"{n} is a digit")
else:
    print(f"{n} is a number")

result="digit" if(n>=-9 and n<=9) else "number"
print(f"{n} is a {result}")