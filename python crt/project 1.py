''' 
WRITE A PYTHON PROGRAM 
1.ADD CONFIRMED GUEST TO THE LIST
2. REMOVE THE GUEST IF THEY ARE NOT ATTNEDING THE PARTY
3.CHECK IF A GUEST IS ON THE LIST OR NOT
4. SORT AND PRINNT THE FINAL GUEST LIST
'''

guest_list=[]
while(True):
    print(".......MENU.............")
    print("1.ADD THE GUEST")
    print("2.REMOVE THE GUEST")
    print("3.CHECK WEATHER THE GUEST IS ATTENDING OR NOT")
    print("4.FINAL LIST OF GUEST")
    print("5.EXIT")
    print("-------------------------------------------------------")

    choice=int(input("ENTER THE OPTION: "))

    if choice==1:
        guest_name=input("ENTER THE GUEST NAME TO ADD: ")
        guest_list.append(guest_name)
        print(f"{guest_name} IS ADDED TO THE GUEST LIST")
    elif choice==2:
        cancel=input("ENTER THE GUEST NAME TO REMOVE: ")
        if cancel in guest_list:
            guest_list.remove(cancel)
            print(f"{cancel} IS REMOVED FROM THE GUEST LIST")
        else:
            print(f"{cancel} IS NOT IN THE GUEST LIST")
    elif choice==3:
        check=input("ENTER THE GUEST NAME TO CHECK: ")
        if check in guest_list:
            print(f"{check} IS IN GUEST LIST")
        else:
            print(f"{check} IS NOT IN THE GUEST LIST")
    elif choice==4:
        if (len(guest_list)==0):
            print("GUEST LIST IS EMPTY")
        else:
            print("HURRAY!! HERE IS YOUR GUEST LIST")
            guest_list.sort()
            print(guest_list)
    elif choice==5:
        print("ENJOY THE PARTY")
        break
    else:
        print("ENTER THE VALID OPTION")

