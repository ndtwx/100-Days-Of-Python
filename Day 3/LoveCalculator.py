print("The Love Calculator is calculating your score...")
name1 = input("Enter the first name") # What is your name?
name2 = input("Enter the second name") # What is their name?

#Combine both name for easier comparing
combined_name = name1 + name2

# make all the letters to lower case
lower_names = combined_name.lower()

# Count the letters within the name
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e 

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e 

#Combine the number in string first then convert back to integer
score = str(first_digit) + str(second_digit)
score = int(score)

#Compare the score 
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else: 
    print(f"Your score is {score}.")





