class Quiz_Brain:
    def __init__(self, questions, answers):
        self.current_question = 0
        self.questions = questions
        self.answers = answers

    def question(self):
        self.current_question += 1
        response = input(f"Q{self.current_question}:{self.questions[self.current_question - 1]}(True/False)?:").lower()
        if response == self.answers[self.current_question - 1]:
            return "Correct"
        else:
            return "Incorrect"
