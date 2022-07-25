import re

question_regex = '[T][0-9][A-Z][0-9][0-9]'
question_list = []
# Writing to a file
#outfile = open('myfile.txt', 'w')
#outfile.writelines((L))
#outfile.close()

#read file
infile = open('rules.txt', 'r')
count = 0
  
while True:
    count += 1
  
    # Get next line from file
    line = infile.readline()
    q_dict = {}
    # if line is empty
    # end of file is reached
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
        
        #print(q_dict)
        question_list.append(q_dict)
        # input("next")
infile.close()
#outfile.close()

print(len(question_list))
count = 1
for dic in question_list:
    print(f"{count} {dic['question_number']}")
    count += 1
