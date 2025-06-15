#a=set()  ----->empty set
set={20,40,45,65,754,54,234,779,786}
print(f"THE ORGINAL SET IS :{set}")
print(type(set))

#membership operator
print(70 in set) #-------> membership operator
print(779 in set)

#using add 
set.add(560)
set.add('slohitha')
print(f"AFTER ADDING AN ELEMNT : {set}")

#using update
set.update(['banana'])
print(f"AFTER UPDATING BANANA :{set}")

#using remove
set.remove('banana')
print(f"AFTER REMOVING BANANA FROM THE SET:{set}")

#pop 
set.pop()
print(f"AFTER USING POP METHOD: {set}")

#discard
set.discard('slohitha')
print(f"AFTER DISCARDING A VALUE:{set}")

#clear
set.clear()
print(f"AFTER CLEARING THE SET :  {set}")

s1={1,2,3}
s2={2,3,6}

#union----->|
print("union")
print(s1|s2)

#intersection---->&
print("intersection")
print(s1&s2)

#difference return 1st elements which are not present in 2
print("DIFFERENCE")
print(s1-s2)

#symmetric difference
print("SYMMETRIC DIFFERENCE")
print(s1^s2)

#methodsof set
print(s1.issubset(s2))
print(s1.intersection(s2))
print(s1.union(s2))
print(s1.difference(s2))
print(s1.issuperset(s2))



