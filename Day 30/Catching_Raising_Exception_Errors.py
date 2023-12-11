"""
< Catching Exceptions >
These are the 4 KEYWORDS that are really important when it comes to handling
1. try: Something that might cause an exception
2. except: Do this if there was an exception
3. else: Do this if there were no exceptions
4. finally: Do this no matter what happens

FileNotFoundError
with open("a_file.txt") as file:
    file.read()

#KeyError
a_dictionary = {"key": "value"}
value = a_dictionary["non_existent_key"]

IndexError
fruits_list = ["Apple", "Banana"]
fruit = fruits_list[2]

TypeError
text = "abc"
print(text + 5)
"""

# try:  # Something that might cause an exception
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["sdfsf"])
# except FileNotFoundError:   # Do this if there was an exception
#     file = open("a_file.txt", 'w')  # If there is an FileNotFoundError it will create the file
#     file.write("Something")
# except KeyError as error_message:  # if you want to get hold of the error message you can do this
#     print(f"The key {error_message} does not exist.")
# else:  # Do this if there were no exceptions
#     content = file.read()
#     print(content)
# finally:  # Do this no matter what happens
#     file.close()
#     print("File was closed.")

"""
Raising your own exceptions
When do you want to raise an error?

when there are certain things that are not caught by the code because it's
perfectly valid code, but it's in fact going to generate the wrong results.
when the result that doesn't make sense

"""
# height = float(input("Height: "))
# weight = int(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Human height should not be more than 3 meters")
#
# bmi = weight / height ** 2
# print(bmi)

"""
Examples
"""
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}]

total_likes = 0
# Catching the KeyError exception in the dictionary
for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass  # You can pass/ignore the keyError so that the code will ignore the dictionary without likes and still calculate the total likes

print(total_likes)
