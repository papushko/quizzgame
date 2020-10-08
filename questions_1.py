questions_file = open('questions.final.txt')
score = 0
total = 6


for line in questions_file:
    if line.startswith('*'):
        print(line[1:])
    if line.startswith('//'):
        print(line[9:])
        ans = input('Answer:')
        ans = ans.split(':')[1]
        if ans.lower() == user :
            score += 1
            print(score)


