# {Key: Value}

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again",
    123: "This is just a number",
    "number": 123456789,
}

#Retrieve a item from the dictionary
print(programming_dictionary["number"])

#Adding new item into the dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"
print(f"{programming_dictionary}\n")

#It can be really useful to start out with a empty dictionary
empty_dictonary = {}

#Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(f"{programming_dictionary}\n")


#Loop through a dictionary
for key in programming_dictionary:
    #Print the key inside the dictionary
    print(key)
    #Print out the value that is associated to the key
    print(programming_dictionary[key])