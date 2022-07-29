from question_model import Question
from quiz_data import QuestionData
from quiz_brain import QuizBrain
from quiz_ui import QuizInterface
from random import shuffle
# import html


quiz = QuestionData()
question_data = quiz.generate_quiz()
#print(len(question_data))

question_bank = []
for question in question_data:
    choices = []
    question_text = question["question_text"]
    correct_answer = question["answer"].lower()
    if correct_answer == "a":
        incorrect_answers = [question["choice_b"],question["choice_c"],question["choice_d"]]
        correct_answer = question["choice_a"]
    elif  correct_answer == "b":
        incorrect_answers = [question["choice_a"],question["choice_c"],question["choice_d"]]
        correct_answer = question["choice_b"]
    elif  correct_answer == "c":
        incorrect_answers = [question["choice_a"],question["choice_b"],question["choice_d"]]
        correct_answer = question["choice_c"]
    else:
        incorrect_answers = [question["choice_a"],question["choice_b"],question["choice_c"]]
        correct_answer = question["choice_d"]
    #incorrect_answers = question["incorrect_answers"]
    for ans in incorrect_answers:
        choices.append(ans)
    choices.append(correct_answer)
    #shuffle(choices)
    new_question = Question(question_text, correct_answer, choices, question["question_number"], question["rule97"])
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

quiz_ui = QuizInterface(quiz)


print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_no}")
