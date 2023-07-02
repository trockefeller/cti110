#CTI-110
#P4HW1 - Score List
#Taylor Rockefeller
#07-02-2023
#
scores = []
num_of_scores = int(input('How many scores do you want to enter? '))
for i in range(1,num_of_scores+1):
    score = float(input(f'Enter score #{i}: '))
    while 0 <= score <= 100:
        scores.append(score)
        break

    else:
        print()
        print('INVALID Score entered!!!!')
        print('Score should be between 0 and 100')
        score = float(input(f'Enter score #{i} again: '))
        continue

scores.sort()
print('---------------Results---------------')
print("Lowest Score  :",min(scores))
scores.pop(0)
print("Modified List :",(scores))
score_avg = sum(scores) / len(scores)
print(f'Scores Average: {score_avg:.2f}')
if score_avg >= 90:
    print('Grade         : A')
elif score_avg >= 80:
    print('Grade         : B')
elif score_avg >= 70:
    print('Grade         : C')
elif score_avg >= 60:
    print('Grade         : D')
else:
    print('Grade         : F')
print('-------------------------------------')
    
    
