print("ENTER TWO SEQUNCES OF EQUAL LENGTH")
s1=input()
s2=input()
if (len(s1)!=len(s2)):
    print("PLEASE ENTER SAME LENGTH OF SEQUNCES")
index=[]
for i in range(len(s1)):
    if (s1[i]!=s2[i]):
        index.append(i)
print(index)

