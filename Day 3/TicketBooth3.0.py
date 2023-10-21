# Ask for the height and age 
height = int(input("What is your height?"))

# Check if the height and age fufill the requirement
price = 0
if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("what is your age?"))
    if age < 12:
        print("Child tickets are $5")
        price = int(5)
    elif age <= 18:
        print("Youth tickets are $7")
        price = int(7)
    else:
        print("Adult tickets are $12")
        price = int(12)
    
    wants_photo = input("Do you want a photo taken? Y or N? ")
    if wants_photo == "Y" or wants_photo == "y":
        price += int(3)
        print("The photo will cost additional $3")
        print(f"Your total bill will be ${price}.")
       
    elif wants_photo == "N" or wants_photo == "n":
        print(f"Your total bill will be ${price}.")
else:
    print("I AM SORRY, YOU ARE TOO SHORT")
