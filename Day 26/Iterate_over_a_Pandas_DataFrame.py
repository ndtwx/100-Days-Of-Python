student_dict = {
    "students": ["Angela", "James", "Lily"],
    "scores": [56, 76, 98]
}

# # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
print("------------------")

# Loop through a data frame
for (key,value) in student_data_frame.items():
    print(value)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # print(row.students)
    # print(row.scores)
    if row.students == "Angela":
        print(row.scores)
