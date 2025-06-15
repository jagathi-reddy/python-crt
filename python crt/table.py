#write a python program to build a function which prints multiplication table of n 
def multi(num):
    for i in range(1, 11):
        print(f"{num} * {i} = {num * i}")

n = int(input("Enter a number: "))
multi(n)