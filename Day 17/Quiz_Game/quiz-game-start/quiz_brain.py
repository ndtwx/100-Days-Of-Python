# todo 1: asking the questions
# todo 2: checking if the answer was correct
# todo 3: checking if we're at the end of the quiz
class QuizBrain:
    def __init__(self, q_list):
        """
        Initialize 3 attributes using init method
        Everytime we create a new QuizBrain object from this class,
        it will have an attribute called question_number with default value of zero
        Same goes to the score

        question_list is going to get it as a value passed over from the question_bank list
        """
        self.score = 0
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        # First get hold of the current question
        current_question = self.question_list[self.question_number]
        # Then +1 to the question number
        self.question_number += 1
        # Ask the user for their answer
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        # Tally the user answer with the correct answer using check_answer method
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")

    def still_has_question(self):
        # Return TRUE if the list is more than the question number
        return self.question_number < len(self.question_list)
