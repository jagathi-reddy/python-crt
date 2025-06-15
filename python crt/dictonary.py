#DICTONARY={KEY1:VALUE1,KEY2:VALUE2,KEY3:VALUE3,........}
#rules
#1.key should be unique
#2.if we mention sam ekey again , the old key will be overwrittem
#3.key should be immutable typ EX:-integer,string,tuple
#we cant use dictonary or list as a keyword
# Initial dictionaries
choclate = {1: '5*', 2: 'dairymilk', 3: 'milkybar', 4: 'barone', 5: 'crispello', 6: 'munch'}
cost = {'5*': 5, 'dairymilk': 10, 'milkybar': 7, 'barone': 8, 'crispello': 20, 'munch': 40}

print("Initial choclate dictionary:", choclate)
print("Initial cost dictionary:", cost)

# Accessing values
print("choclate[5]:", choclate[5])
print("choclate[3]:", choclate[3])
print("cost['5*']:", cost['5*'])
print("cost['munch']:", cost['munch'])

# Updating values
choclate[5] = 'kitkat'
cost['milkybar'] = 14
print("Updated choclate:", choclate)
print("Updated cost:", cost)

# Adding new items
choclate[7] = 'nutties'
print("Added choclate[7]:", choclate[7])

# Removing items
choclate.pop(4)
del choclate[5]
print("After removing keys 4 and 5:", choclate)

# Length
print("Length of choclate dictionary:", len(choclate))

# Keys, values, and items
print("Keys:", choclate.keys())
print("Values:", choclate.values())
print("Items:", choclate.items())

# Copying
c = choclate.copy()
d = cost.copy()
print("Copied choclate dictionary:", c)
print("Copied cost dictionary:", d)

# Update with another dictionary (Note: keys will be overwritten if they match)
d.update(c)
print("After updating cost with choclate:", d)

# --- Missing Operations ---

# get() method (safe access)
print("choclate.get(3):", choclate.get(3))
print("choclate.get(10, 'Not Found'):", choclate.get(10, 'Not Found'))

# setdefault()
print("Using setdefault for key 8:", choclate.setdefault(8, 'perk'))
print("Updated choclate with setdefault:", choclate)

# fromkeys() - creates a new dictionary from keys with the same default value
keys = ['kitkat', 'munch', '5*']
new_dict = dict.fromkeys(keys, 100)
print("New dictionary from keys:", new_dict)

# popitem() - removes and returns the last inserted key-value pair
last_item = choclate.popitem()
print("Removed last item using popitem:", last_item)
print("choclate after popitem:", choclate)

# clear() - removes all items
empty_dict = new_dict.copy()
empty_dict.clear()
print("Cleared dictionary:", empty_dict)

# Loop through dictionary
print("Looping through choclate dictionary:")
for k, v in choclate.items():
    print(f"Key: {k}, Value: {v}")

