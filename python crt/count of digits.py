n=int(input("ENTER THE NUMBER: "))
x=0
temp=n
n=abs(n)
while (n!=0):
    n=n//10
    x+=1
print(f"{temp} has {x} digits")