# Take note that position 0 counts from before "a"
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]

# Get all the items in the list up after position 2 till position 5
print(piano_keys[2:5])

# Get all the items in the list up after position 1
print(piano_keys[1:])

# Get all the items in the list up to position 5
print(piano_keys[:5])

# Get all the items in the list up after position 2 till position 5 by increment of 2
print(piano_keys[2:5:2])

# Get all the items in the list up from beginning to the end by increment of 2
print(piano_keys[::2])

# Reverse the list
print(piano_keys[::-1])

# Slicing work with tuples as well
piano_tuple = ["do", "re", "mi", "fa", "so", "la", "ti"]

print(piano_tuple[2:5])

