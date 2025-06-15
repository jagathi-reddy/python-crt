''' 
1. TO DISPLAY THE MENU OF FOOD IYTEMS
2. CREATE A TUPPLE OF PRICES WITH RESPCT TO FOOD ITEMS LIST
3. READ THE INPUT FROM THE USER FOR ODERING FOOD INCLUDING THE QUAANTITY
      IF IT EXIST IN THE MENU ----CONFIRM ORDER
      IF NOT PRINT A MESSAGE 
4.WHILE BILLING , READ PH NO, FEEDBACK ,READ TIP AMOUNT,
5.ADD 18% GST TO THE BILL & PRINT THE BILL IF BILL>0
'''

print("==========MENU=======")
print("IDLY   ₹20")
print("DOSA   ₹30")
print("POORI  ₹40")
print("UGGANI ₹35")
print("VADA   ₹20")
print("UPMA   ₹50")
print("UTAPPA ₹50")
print("==========****=======")

n=int(input("ENTER THE NUMBER OF ITEMS YOU ARE GOING TO ORDER:" ))
tiffins=['idly','dosa','poori','uggani','vada','upma','utappa',]
prices=(20,30,40,35,20,50,50)
i=1
bill=0
while(i<=n):
    choice=input("ENTER THE BREAKFAST YOU REQUIRED : ")
    if choice in tiffins:
        index=tiffins.index(choice)
    else:
        print("ITEM IS NOT AVAILABLE")
    bill+=prices[index]
    i+=1

print("THANK YOU FOR ORDERING....!!!!")
print("BILLING IS GOING ON PLEASE PROVIDE THE REQUIRED DETAILS")
ph=input("ENTER YOUR 10 DIGITS PHONE NUMBER : ")
feedback=input("PLEASE PROVIDE YOUR VALUABLE FEEDBACK:")
tip=int(input("PLEASE ENTER THE TIP AMOUNT :"))
if bill>0:
    bill = bill+bill*0.18 + tip
print("HERE IS YOUR FINAL BILL...!!!")
print(f"{bill} INR")


   

