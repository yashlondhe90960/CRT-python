
my_set = {1, 2, 3, 4, 5}

print(my_set)


my_set.add(6)
print(my_set)


my_set.remove(3)

# # Check if an element is in the set
if 4 in my_set:
    print("4 is in the set")
else:
    print("4 is not in the set")

# # Get the length of the set
set_length = len(my_set)
print("Length of the set:", set_length)

# # Iterate over the set
for element in my_set:
    print(element)