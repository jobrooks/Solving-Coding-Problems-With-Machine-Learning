# 1.7 wrong answer 0/7
import sys

problems = {}
penalties = {}
solved = 0
time = 0

while True:
    line = input().split()
    if line[0] == '-1':
        break
    
    minutes = int(line[0])
    problem = line[1]
    result = line[2]
    
    if problem not in problems:
        problems[problem] = 0
        penalties[problem] = 0
    
    if result == 'right':
        solved += 1
        time += minutes + penalties[problem]
        problems[problem] = 1
    else:
        penalties[problem] += 20

for problem in problems:
    if problems[problem] == 1:
        time += penalties[problem]

print(solved, time)
