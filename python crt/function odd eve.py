num = int(input("Enter an integer: "))

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

result = check_even_odd(num)
print(f"{num} is {result}")


#write a pyhon progrm check wether the user given number is prime number or not using functions using return
def prime(num):
    count =0
    for i in range(2,num+1):
        if num % i == 0:
            count+=1
    if count==1:
         print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")
        

           

num = int(input("Enter an integer: "))
print(prime(num))


