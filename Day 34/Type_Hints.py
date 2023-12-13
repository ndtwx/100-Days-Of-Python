"""
Set the data type for the variable to prevent data type error
"""
# age: int
# name: str
# height: float
# is_human: bool

# age = 10
# age = "ten"

"""
Can also specify data type in function
as well as specify output data type

"""
def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive
    # return "can_drive"


if police_check(12):
    print("You may pass")
else:
    print("Pay a fine.")







