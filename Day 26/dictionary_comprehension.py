"""
Creating new dictionary with the dictionary comprehension method
LIST can be any sort of iterable; a list, a range, a string

1. new_dict = {NEW_KEY:NEW_VALUE for ITEM in LIST}

"""
"""
Create a new dictionary based on the values in an EXISTING dictionary 
by getting hold of all of the items inside and split it into a KEY and a VALUE

Loop through each of the KEYS and VALUES in all of the items in the dictionary
and we can use these KEYS and VALUES VARIABLE to create a NEW_KEYS and NEW_VALUE

2. new_dict = {new_key:new_value for (key,value) in dict.items()} 
"""
"""
Add a condition at the end depending on situation 

3. new_dict = {new_key:new_value for (key,value) in dict.items() if test}
"""
import random

names = ["Alex", "Beth", "Caroline", "Dave", "Andy", "Qiyang", "Jerene", "ShiYing", "JianHao"]
# Creating a new dictionary
# NEW_DICT = {NEW_KEY:NEW_VALUE for ITEM in LIST}
student_scores = {student: random.randint(40, 100) for student in names}
print(student_scores)

# Creating another NEW dictionary using EXISTING dictionary data
# NEW_DICT = {NEW_KEY:NEW_VALUE for (KEY,VALUE) in DICT.ITEMS() if TEST}
passed_students = {student: score for (student, score) in student_scores.items() if score >= 50}
print(passed_students)

"""
1. Split each word in the sentence string
2. Loop through each word and calculate the number of letters in each word
3. Store the word and the number of letters into NEW_KEYS:NEW_VALUE to a new dictionary 
"""
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# NEW_DICT = {NEW_KEY:NEW_VALUE for ITEM IN LIST}
result = {word: len(word) for word in sentence.split()}
print(result)

"""
You can get each of the items from a dictionary using the .items() method: 
https://www.w3schools.com/python/ref_dictionary_items.asp
"""
# Convert celsius  to fahrenheit
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# NEW_DICT = {NEW_KEY:NEW_VALUE for ITEM IN LIST}
weather_f = {day: temp * 9/5 + 32 for (day,temp) in weather_c.items()}
print(weather_f)
