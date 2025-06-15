n=int(input("ENTER THE NUMBER : "))
temp = n
x=0
r=0
n = abs(n)
while n!=0:
    r=n%10
    x=x+r
    n=n//10
print(f"summation of digits of {temp} is {x}")


    