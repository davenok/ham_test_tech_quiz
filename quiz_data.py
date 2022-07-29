import re
import json
import random
from pprint import pprint


class QuestionData:
    def __init__(self):
        question_regex = '[T][0-9][A-Z][0-9][0-9]'
        self.question_pool = []
        self.test_questions = []
        self.question_num = 0

        infile = open('rules.txt', 'r')
        
        while True:
            line = infile.readline()
            q_dict = {}
            if not line:
                break
            elif re.match(question_regex, line):
                foo = line.split(' ') 
                q_dict["question_number"] = foo[0]
                q_dict["answer"] = foo[1].strip("()")
                if len(foo) == 3:
                    q_dict["rule97"] = foo[2].strip('\n')
                else:
                    q_dict["rule97"] = ''
                q_dict["question_text"] = infile.readline().strip('\n')
                q_dict["choice_a"] = infile.readline().strip('\n')[3:]
                q_dict["choice_b"] = infile.readline().strip('\n')[3:]
                q_dict["choice_c"] = infile.readline().strip('\n')[3:]
                q_dict["choice_d"] = infile.readline().strip('\n')[3:]
                
                self.question_pool.append(q_dict)
        infile.close()
        random.shuffle(self.question_pool)

        #35 questions - by category  6,3,3,2,4,4,4,4,2,3
        for q in self.get_section_questions("T1",6):
            self.test_questions.append(q)
        for q in self.get_section_questions("T2",3):
            self.test_questions.append(q)
        for q in self.get_section_questions("T3",3):
            self.test_questions.append(q)
        for q in self.get_section_questions("T4",2):
            self.test_questions.append(q)
        for q in self.get_section_questions("T5",4):
            self.test_questions.append(q)
        for q in self.get_section_questions("T6",4):
            self.test_questions.append(q)
        for q in self.get_section_questions("T7",4):
            self.test_questions.append(q)
        for q in self.get_section_questions("T8",4):
            self.test_questions.append(q)
        for q in self.get_section_questions("T9",2):
            self.test_questions.append(q)
        for q in self.get_section_questions("T0",3):
            self.test_questions.append(q)
        random.shuffle(self.test_questions)




    def get_section_questions(self, section, count):
        section_questions = []
        my_list = list(
            filter(
                lambda item: item["question_number"].startswith(section), self.question_pool
                )
            )
        random.shuffle(my_list)
        for q in range(0,count):
            section_questions.append(my_list[q])
        return section_questions

    def generate_quiz(self):
        return self.test_questions

    






        # #35 questions - by category  6,3,3,2,4,4,4,4,2,3
        # for q in self.get_section_questions("T1",6):
        #     self.test_questions.append(q)
        # for q in self.get_section_questions("T2",3):
        #     self.test_questions.append(q)
        # for q in self.get_section_questions("T3",3):
        #     self.test_questions.append(q)
        # for q in self.get_section_questions("T4",2):
        #     self.test_questions.append(q)
        # for q in self.get_section_questions("T5",4):
        #     self.test_questions.append(q)
        # for q in self.get_section_questions("T6",4):
        #     self.test_questions.append(q)
        # for q in self.get_section_questions("T7",4):
        #     self.test_questions.append(q)
        # for q in self.get_section_questions("T8",4):
        #     self.test_questions.append(q)
        # for q in self.get_section_questions("T9",2):
        #     self.test_questions.append(q)
        # for q in self.get_section_questions("T0",3):
        #     self.test_questions.append(q)
        #     print(len(self.test_questions))


# print(len(test_questions))
#question_data = json.dumps(test_questions)

# pprint(question_data)

# ORIGINAL CODE BELOW
# import requests

# parameters = {
#     "amount": 10,
#     "type": "multiple"
# }

# response = requests.get(url="https://opentdb.com/api.php", params=parameters)
# question_data = response.json()["results"]


# """
# Sample Response

# [
#     {
#         'category': 'Sports', 
#         'type': 'multiple', 
#         'difficulty': 'medium', 
#         'question': 'Which Formula One driver was nicknamed &#039;The Professor&#039;?',
#         'correct_answer': 'Alain Prost', 
#         'incorrect_answers': [
#             'Ayrton Senna', 
#             'Niki Lauda', 
#             'Emerson Fittipaldi'
#             ]
#     }, 
#     {
#         'category': 'Entertainment: Music', 
#         'type': 'multiple', 
#         'difficulty': 'medium', 
#         'question': 'In which city did American rap producer DJ Khaled originate from?',
#         'correct_answer': 'Miami', 
#         'incorrect_answers': [
#             'New York', 
#             'Detroit', 
#             'Atlanta'
#             ]
#         }
# ]
# """
