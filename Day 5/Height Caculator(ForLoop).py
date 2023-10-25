
# Input a Python list of student heights

print("Please enter the height of each student with a space between each height.")
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
average_height = 0
total_student = 0

# Caculate the number of students according to the number of index value
for x in student_heights:
  total_student +=1

# Caculate the total height of all the students
for height in student_heights:
  total_height += height

average_height = total_height / total_student

print(f"total height = {total_height}")
print(f"number of students = {total_student}")
print(f"average height = {round(average_height)}")