n=int(input("ENTER TYE SIZE OF ARRAY: "))

list=[]
multiples=[]

for i in range(n):
    element=int(input(f"ELEMENT AT {i+1} is "))
    list.append(element)

for i in list:
    if i%15==0:
        multiples.append(i)
print(multiples)
