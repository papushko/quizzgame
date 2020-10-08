print('Welcome to Trivia')

question_file = open('questions.final.txt')

score = 0
no_of_questions = 6



for line in question_file:
    #1
    line = line.rstrip()
    if line.startswith('*'):
        print(line[1:])
    else:
        if line.startswith('/'):
            actual_answer = line.split(':')[1]
            user_answer = input('Answer:')
            if actual_answer == user_answer:
                score += 1



    if line.startswith('#'):
        print(line[1:])
        if line.startswith('//'):
            actual_answer = line.split(':')[1]
            user_answer = input('Answer:')
            if actual_answer == user_answer:
                score += 1



print(score)







