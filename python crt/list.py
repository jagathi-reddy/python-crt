# Creating a list
my_list = [10, 20, 30, 40, 50]
print("Original list:", my_list)

# Append - adds an element at the end
my_list.append(60)
print("After append(60):", my_list)

# Extend - adds elements from another iterable
my_list.extend([70, 80])
print("After extend([70, 80]):", my_list)

# Insert - inserts element at specific index
my_list.insert(2, 25)
print("After insert(2, 25):", my_list)

# Remove - removes the first matching value
my_list.remove(40)
print("After remove(40):", my_list)

# Pop - removes and returns element at given index (default: last)
popped = my_list.pop()
print("After pop():", my_list, " -> Popped:", popped)

# Index - returns the first index of a value
index = my_list.index(30)
print("Index of 30:", index)

# Count - counts how many times an element appears
count = my_list.count(20)
print("Count of 20:", count)

# Reverse - reverses the list in place
my_list.reverse()
print("After reverse():", my_list)

# Sort - sorts the list in ascending order
my_list.sort()
print("After sort():", my_list)

# Copy - creates a shallow copy
copy_list = my_list.copy()
print("Copy of the list:", copy_list)

# Clear - removes all items from the list
copy_list.clear()
print("After clear() on copy_list:", copy_list)

# Slicing - getting sublists
print("Slicing [1:4]:", my_list[1:4])
print("Slicing with step [::2]:", my_list[::2])

# List concatenation
new_list = my_list + [100, 200]
print("After concatenation:", new_list)

# Membership testing
print("Is 50 in my_list?", 50 in my_list)
print("Is 99 in my_list?", 99 in my_list)

# Length of list
print("Length of my_list:", len(my_list))
