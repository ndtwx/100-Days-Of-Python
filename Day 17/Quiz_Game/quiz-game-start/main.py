from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Empty list used to contain a list of question objects
question_bank = []

'''
Loop through each question inside the question_data list 
and create a variable for each question which comes from the question 
dictionary. Same goes for the answer
'''
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    # Create a new Question object and save it into the variable
    new_question = Question(question_text, question_answer)
    # Append into the empty list
    question_bank.append(new_question)


# Create a QuizBrain object and pass in  a list of question
# from the question_bank list as the argument
quiz = QuizBrain(question_bank)

# While there are still question remaining run the next_question() method
while quiz.still_has_question():
    quiz.next_question()


print("You have completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number} ")
