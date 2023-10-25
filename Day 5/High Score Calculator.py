# Input a list of student scores
# student_scores = input().split()
student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇

highest_score = 0

# Check if the current highest score is higher than the next score. If yes, replace the current highest score
for score in student_scores:
  if score > highest_score:
    highest_score = score
    
print("The highest score in the class is:", highest_score)
  
