from question_model import Question
from data import question_data
from quiz_brain import Quiz_Brain

questions = []
answers = []
for question in question_data:
    ques = question["text"]
    ans = question["answer"]
    new_question = Question(ques, ans)
    questions.append(new_question.text)
    answers.append(new_question.answer)

quiz = Quiz_Brain(questions, answers)
while True:
    result = quiz.question()
    if result == "Incorrect":
        print("Incorrect")
        print(f"You answered {quiz.current_question - 1} questions correctly")
        break
    else:
        print(result)
