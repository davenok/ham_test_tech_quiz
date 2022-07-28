import re
import json
import random
from pprint import pprint

question_regex = '[T][0-9][A-Z][0-9][0-9]'
question_pool = []

infile = open('rules.txt', 'r')
  
while True:
    line = infile.readline()
    q_dict = {}
    if not line:
        break
    elif re.match(question_regex, line):
        foo = line.split(' ') 
        q_dict["question_number"] = foo[0]
        q_dict["answer"] = foo[1]
        if len(foo) == 3:
            q_dict["rule97"] = foo[2].strip('\n')
        else:
            q_dict["rule97"] = ''
        q_dict["question_text"] = infile.readline().strip('\n')
        q_dict["answer_a"] = infile.readline().strip('\n')
        q_dict["answer_b"] = infile.readline().strip('\n')
        q_dict["answer_c"] = infile.readline().strip('\n')
        q_dict["answer_d"] = infile.readline().strip('\n')
        
        question_pool.append(q_dict)
infile.close()

# print(f"{len(question_list)} questions read from file")
# count = 1
# for dic in question_list:
#     print(f"{count} {dic['question_number']}")
#     count += 1

#35 questions - by category  6,3,3,2,4,4,4,4,2,3

group = "T1"
my_list = list(
    filter(
        lambda item: item["question_number"].startswith(group), question_pool
        )
    )

pprint(my_list)

section_list = []

for q in range(1,7):
    section_list += random.choice(my_list)


print(section_list)
#question_data = json.dumps(question_list)

#print(question_data)

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
