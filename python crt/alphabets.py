'''
write a python programe to read a trsing as input from the user and print the count of 
1.UPPERCASE VOWELS
2.LOWERCASE VOWELS
3.UPPERCASE CONSONANTS
LOWECASE CONSONATS
'''

s=input("ENTER A STRING: ")
uppervowel=0
lowervowel=0
lowerconsonant=0
upperconsonant=0
for ch in s:
    if (ch>='A' and ch<='Z'):
        if ch in 'AEIOU':
            uppervowel+=1
        else:
            upperconsonant+=1
    elif(ch>='a' and ch<='z'):
        if ch in 'aeiou':
            lowervowel+=1
        else:
            lowerconsonant+=1

print(f" THE NO.OF UPPER CASE VOWELS IN {s} ARE : {uppervowel}")
print(f" THE NO.OF LOWER CASE VOWELS IN {s} ARE : {lowervowel}")
print(f" THE NO.OF UPPER CASE CONSONANTS IN {s} ARE : {upperconsonant}")
print(f" THE NO.OF UPPER CASE CONSONANTS IN {s} ARE : {lowerconsonant}")





