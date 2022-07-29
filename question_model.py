class Question:
    def __init__(self, question: str, correct_answer: str, choices: list, qnum: str, rule97: str):
        self.question_text = question
        self.correct_answer = correct_answer
        self.choices = choices
        self.qnum = qnum
        self.rule97 = rule97