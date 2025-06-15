s=input("ENTER THE DNA SEQUENCE:")
#gc=0
print(f"USER ENTERED DNA SEQUENCE IS : {s}")
g=s.count('G')
c=s.count('C')
p= ((g+c)/len(s))*100
'''for i in s:
    if (i=='G' or i=='C'):
        gc+=1
p=float (gc/len(s))*100'''
print(f"THE GC% IN GIVEN SEQUENCE IS :{p}% ")
if p>60:
    print("HIGH GC")
elif (p>=40 and p<=60):
    print("MODERATE GC")
else:
    print("LOW GC")

