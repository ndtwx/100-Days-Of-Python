# Ask for the height and age 
height = int(input("What is your height?"))
age = int(input("What is your age?"))

# Check if the height and age fufill the requirement
if height > 120:
    if age < 12:
        print("Please pay $5")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("I AM SORRY, YOU ARE TOO SHORT")