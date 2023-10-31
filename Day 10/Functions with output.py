#Function with Outputs
#'return' tells the computer that it is the end of the code and should exit the function
#so any code that comes after it will be ignored 
def format_name_v1(f_name_v1, l_name_v1):
    first_name_v1 = f_name_v1.title()
    last_name_v1 = l_name_v1.title()
    return f"{first_name_v1} {last_name_v1}"

print(format_name_v1("AnDy","tAnG"))


#Function with more than one return
def format_name_v2(f_name_v2, l_name_v2):
    if f_name_v2 == "" or l_name_v2 == "":
        #This return will make the computer to skip the remaining code if the if statement is fufill
        return "You didn't provide valid inputs"
    first_name_v2 = f_name_v2.title()
    last_name_v2 = l_name_v2.title()
    return f"{first_name_v2} {last_name_v2}"

print(format_name_v2(input("What is your first name?\n"),input("What is your last name?\n")))
