'''
write a python program to declare a list of grocerry items and create the input read the input fromm the user from one to five 
1. to display the list of grocerry items in sorted way
2 .to take the input from the userr and add items to the cart
3 .to give the cart items
4 .to update the quantity ar item present in the cart
5 .generare a bill including item name, quantity, price and if the final bill amount is greater than 1000 then the user will get 10 $discount
6.if the user purchases any item more than 10 kg reduce the amout of 1kg frm that particular items price 
7.if the user purchase any particular product add buy one get one free offer to it
8.so add 25% gst to the overall bill and print the final bill
9.other than 1-5 options print a message that the option is not available
10.fter printing bill exit the program
'''
raw=['flours','liquids','grains','dals','read to eat']
print("=========CATEGORY========")
print("1.FLOURS")
print("2.LIQUIDS")
print("3.GRAINS")
print("4.DALS")
print("5.RAEDY TO EAT")
print("=========********========")
n= int(input("PLEASE SELECT THE REQUIRED SECTION YOU WOULD LIKE TO SHOP: "))
if n==1:
    flours=['wheat','jowar','rice','besan','corn flour','maida']
    cost=[40,50,30,60,70,45]
    print("ITEM - COST/KG")
    print("WHEAT - 40")
    print("JOWAR - 50")
    print("RICE  - 30")
    print("BESAN - 60")
    print("CORN  - 70")
    print("MAIDA - 45")
    fl=input("PLEASE SELECT THE ITEM TO ADD INTO THE CART: ")
    i=flours.index(fl)
    print(f"THE COST OF {fl} is {cost[i]}")

    