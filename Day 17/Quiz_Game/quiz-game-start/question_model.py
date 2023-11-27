"""
Each question contains two attributes:
self.text
self.answer

These two attributes are going to be initialized

When creating an object we will be using them to retrieve the question and answer
new_question = Question(text, answer)
"""


class Question:
    def __init__(self, text, answer):
        # Initialize 2 attributes using init method
        self.text = text
        self.answer = answer
