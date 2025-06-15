'''
write a python program to take name as input from the user including prefix as (either mr/ms/mrs) print the gender classification of the name on basis of prifix
'''
s=input("ENTER THE FULL NAME INCLUDING MR/MS/MRS : ")
if s.startswith("mr"):
    print("male")
elif s.startswith("ms"):
    print("female")
else:
    print("ENTER THE VALID NAME WITH PREFIX")
