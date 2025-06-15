num=[12,34,56,75,45,45,65,56,89,44,54]
print("ORGINAL LIST")
print(num)
new_l=[]
for i in num:
    if i not in new_l:
        new_l.append(i)

print("AFTER REMOVING DUPLICATES")
print(new_l)
