s=int(input("ENTER THE COUNT OF DATA: "))
values=[]
for i in range (s):
    n=float(input(f"ENTER THE {i+1} number :"))
    values.append(n)
output=[]
print(f"USER ENTERED VALUES ARE {values}")
for i in values:
    if i<5:
        output.append("UNDER EXPRESSED")
    elif (i>=5 and i<=15):
        output.append("NORAML")
    else:
        output.append("OVER EXPRESSED")
print(output)
