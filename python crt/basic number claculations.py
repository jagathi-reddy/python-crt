n=int(input("ENTER THE NUMBER :"))
print("NATURAL  NUMBERS FROM 1 TO {n}")
for i in range (1,n+1):
    print(i)


print("NATURAL NUMBERS FROM {n} to 1")
for i in range (n,0,-1):
    print(i)

print("SQUARES FROM 1 TO {n}")
for i in range (1,n+1):
    print(i*i)