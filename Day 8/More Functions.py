#Require two parameters
def greet(name, location):
    print(f"Hello {name}")
    print(f"How is the weather like in {location}?")

greet("Andy","Singapore")
greet(name="Andy",location="Singapore")
greet(location="Singapore",name="Andy")

print("----------------------------------------------------------")

import math
def paint_calc(height,width,cover):
    number_of_cans = ((height * width) / cover)
    #Round up the float with math.ceil function
    print(f"You'll need {math.ceil(number_of_cans)} cans of paint.")


test_h = int(input("Enter the height of the wall: ")) # Height of wall (m)
test_w = int(input("Enter the width of the wall: ")) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
