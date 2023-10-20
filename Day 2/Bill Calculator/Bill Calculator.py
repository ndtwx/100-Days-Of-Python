#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

# Calculate the amount of tip percentage 
total_tip_amount = bill * (tip / 100)

# Calculate the total bill including the tip
total_bill = bill + total_tip_amount

# Split the total bill depending on the amount of people 
bill_per_person = total_bill / people

# Round up the final amount to 2 decimal place
final_amount = round(bill_per_person, 2)

# Using f string to print out
print(f"Each person will pay: ${final_amount}")

# FAQ: How to round to 2 decimal places?

# Find the answer in the Q&A here: https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132#questions/13315048
