#Use for create documentation for each function or in other blocks of code
#Starts with """ and end with """
#Allow you to write multiple sentences in new line without error
#When you call for the function, it will show the documentation telling you what is it for

#Example:
def format_name_v2(f_name_v2, l_name_v2):
    """Take a first and last name and format it 
    to return the title case version of the name."""
    if f_name_v2 == "" or l_name_v2 == "":
        #This return will make the computer to skip the remaining code if the if statement is fufill
        return "You didn't provide valid inputs"
    first_name_v2 = f_name_v2.title()
    last_name_v2 = l_name_v2.title()
    return f"{first_name_v2} {last_name_v2}"


