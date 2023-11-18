############DEBUGGING#####################

"""
1. Describe the Problem
2. Reproduce the Bug
3. Pretend to be the Computer
4. Fix the errors shown on the editor immediately 
5. Use the Print function
6. Use a Debugger
7. Run your code often
8. Ask StackOverFlow :) 
"""
# Debug 1
# # Describe Problem
# What is the for-loop doing?
# When is the function meant to print "You got it"?
# What are your assumptions about i?

"""
Return an object that produces a sequence of integers from start (inclusive) to stop (exclusive) by step. 
range(i, j) produces i, i+1, i+2, ..., j-1. start defaults to 0, and stop is omitted! 
range(20) produces 0 to 19 only
"""
# # Wrong code
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

# # Correct code
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()
#-----------------------------------------------------------------------------------------
# Debug 2
# # Reproduce the Bug
"""
Always run your code at least 10 times to make sure it is really working,
if error do occur reproduce the Bug to see if the error is consistent before trying to debug it

"randint" return random integer in range [a, b], including both end points.
for a list it always starts from 0. If you try to pick out of the list,
you will get an error.
"""
# # Wrong code
# from random import randint
# #             0 ,  1 ,  2 ,  3 ,  4 ,  5
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# Correct code
from random import randint
# #             0 ,  1 ,  2 ,  3 ,  4 ,  5
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

#-----------------------------------------------------------------------------------------
# Debug 3
# # Play Computer
"""
Reason is because this skill of pretending to be a computer reading
through your code and imagining what you going to do each time is really,
really useful, especially when you're debugging.

When there's both TRUE and FALSE in a "and" Condition. it will result to FALSE
"""
# # Wrong code
# year = int(input("What's your year of birth?"))
# year = 1994
"""
if year = 1994
1994 > 1980(TRUE) and 1994 < 1994(FALSE)
TRUE and FALSE = FALSE
"""
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
"""
# FALSE since 1994 is not greater but equal to 1994
"""
# elif year > 1994:
#   print("You are a Gen Z.")
  
# # Correct Code
# year = int(input("What's your year of birth?\n"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")

#-----------------------------------------------------------------------------------------
# Debug 4
# # Fix the Errors
"""
When the editor's giving you an error or when the console is giving you an error, 
fix the errors before you continue. 
Now, this is a little bit easier when you're dealing with errors in the editor,
because it will actually highlight to you the line that's broken.

However, some error will not show until you run your code.
For example:
<TypeError: '>' not supported between instances of 'str' and 'int'>
Reason: 
You are getting the input as a string so you must cast that string to an int object 
in order to do numerical operations 
"""
# # Wrong code 
# age = input("How old are you?")
# # if age > 18: 
# print("You can drive at age {age}.")
# else:
#    print("You are underage!")

# # Correct code
# age = int(input("How old are you?\n"))
# if age > 18:
#     print(f"You can drive at age {age}.")
# else:
#     print("You are underage!")
#-----------------------------------------------------------------------------------------
# Debug 5
# #Print is Your Friend
"""
Print function can help you debug your code,
which is a pretty decent thing for it to do.
"""
# # Wrong code 
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: ")) << there's two equal sign instead of one
# print (f"pages = {pages}") 
# print (f"word_per_page = {word_per_page}") 
# total_words = pages * word_per_page
# print(total_words)

# Correct code
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)
#-----------------------------------------------------------------------------------------
# Debug 6
# #Use a Debugger
"""
https://pythontutor.com/python-compiler.html#mode=edit

You can put a breakpoint in most debuggers, 
which tells the computer to stop what you're doing at this particular line.
And then at that moment in time,
I want to examine what all the variables and all the functions are doing.
If you click on a certain line of code, you can see it becomes red
"""

"""
The problem is that when we are adding the new item to the b_list 
<b_list.append(new_item)>
we're doing it outside of the for loop.
It's when this loop has completed and at the very end
do we actually call this line.
So what we needed to do to fix this code is just to indent that line over.
"""
# Wrong code
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])

# Correct code
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])