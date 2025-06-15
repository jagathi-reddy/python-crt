def eat():
    def wash():
        print("WASH YOUR HANDS......!")
    def serve():
        print("SERVE FOOD")
    wash()
    serve()
    print("ENJOY YOUR MEAL")
    wash()
eat()

def hello():
    return "HELLO"
s=hello()
print(s)
print(hello())

#- FORMAL ARGUMENT - FUNCTION DEFINITION PARAMETERS 

def pw(x,y):
    z=x**y
    print(z)
pw(5,2)

def show(name,age):
    print(name,age)
show(name="ram",age=62)

def display(*x):
    x=x[0]+x[1]+x[2]+x[3]+x[4]
    print(x)
display(10,20,30,40,50,60)
