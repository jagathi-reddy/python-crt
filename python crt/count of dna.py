s=input("enter the sample base value:")
'''base={1:'A',2:'C',3:'T',4:'G'}
A,G,C,T=0,0,0,0
for i in s:
    if i in base[1]:
        A+=1
    if i in base[2]:
        C+=1
    if i in base[3]:
        T+=1
    if i in base[4]:
        G+=1
count={'A':A,'C':C,'G':G;'T':T}'''
#method2
A=s.count('A')
G=s.count('G')
C=s.count('C')
T=s.count('T')
count={'A':A,'C':C,'G':G,'T':T}
print(count)

#method3
count={{'A':A,'C':C,'G':G,'T':T}}




