print("--------------------------------------------------------------")
print("BMI under 18.5 are underweight.")
print("BMI over 18.5 but below 25 have a normal weight.")
print("BMI equal to or over 25 but below 30 are slightly overweight.")
print("BMI equal to or over 30 but below 35 are obese.")
print("BMI equal to or over 35 are clinically obese.")
print("--------------------------------------------------------------")
# Enter your height in meters e.g., 1.55
height = float(input("What is your height?"))

# Enter your weight in kilograms e.g., 72
weight = int(input("What is your weight?"))

# 🚨 Don't change the code above 👆

# #Write your code below this line 👇
bmi = weight / (height**2)

if bmi < 18.5:
    print(f"Your BMI is {round(bmi,2)}, you are underweight.")
elif bmi  < 25:
    print(f"Your BMI is {round(bmi,2)}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {round(bmi,2)}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {round(bmi,2)}, you are obese.")
else:
    print(f"Your BMI is {round(bmi,2)}, you are clinically obese.")


