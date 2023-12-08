"""
WHAT IS LIST COMPREHENSION?

create a new list from a previous list.

using the keyword method where you type out the list comprehension keywords
and the replace each of the words  with the actual item in your  code

new list = [new_item for item in list]
"""
numbers_1 = [1,2,3]
new_list_1 = []
for n_1 in numbers_1:
    add_1 = n_1 + 1

# is the same as

numbers = [1,2,3]
# new list = [new_item for item in list]
new_list = [n+1 for n in numbers]
print(new_list)

name = "Andy"
letters_list = [letter for letter in name]
print(letters_list)

range_list = [ num * 2 for num in range(1,5)]

# Conditional List Comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# NEW_LIST = [<NEW_ITEM> for <ITEM> in <LIST> if <TEST>]
short_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) > 5]
print(short_names)
print(long_names)
