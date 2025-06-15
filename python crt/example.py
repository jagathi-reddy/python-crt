''' 
write a python programme to decalre a list of word and declare a tuple of words and map it to print the combined word

list=['marker','water','bread','class','wrist','black','nail','krack']
tuple=('pen','bottle','jam','room','watch','board','paint','jack')
word=input("ENTER THE WORD: ")
index=list.index(word)
print(f"{word}-{tuple[index]}")
'''

s=input("ENTER THE STRING:")
print(f"USER ENTERED STFRING :{s}")
s1=s.split()
s2=''.join(s1)
print(f"STRING WITHOUT SPACES: {s2}")





