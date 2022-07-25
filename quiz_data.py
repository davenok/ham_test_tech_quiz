import re

question_regex = '[T][0-9][A-Z][0-9][0-9]'
question_list = []

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
        
        question_list.append(q_dict)
infile.close()

print(f"{len(question_list)} questions read from file")
count = 1
for dic in question_list:
    print(f"{count} {dic['question_number']}")
    count += 1


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
