# fruits =["strawberries", "Apples", "Grapes", "Peaches"]
# vegetables = ["Spinach","Kale","Tomatoes","Celery","Potatoes"]

# dirty_dozen = [fruits, vegetables]

# print(dirty_dozen[1][1])

line1 = ["⬜","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to hide your treasure?\n") # Where do you want to put the treasure?

letter = position[0].lower() # Convert the first position of the input (which is a letter) to lowercase
abc = ["a", "b", "c"] # Create a list to represnt the possible letters 

letter_index = abc.index(letter) # Using .index() function to get the position value of the letter
number_index = int(position[1])-1 # Get the second position value of the input(which is a number), minus 1 because the list starts from 0 

# Replace the box(index) with a "X" (Nested Lists in Python are accessed from outside to inside therefore it starts with number_index because map is at the most outside) 
map[number_index][letter_index] = "X"

print("------------------")
print(f"{line1}\n{line2}\n{line3}")
print("------------------")
