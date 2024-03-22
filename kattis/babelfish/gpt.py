# 2.2 accepted 2/2

dictionary = {}

# read in the dictionary
while True:
    line = input().strip()
    if line == "":
        break
    english, foreign = line.split()
    dictionary[foreign] = english

# translate the message
while True:
    try:
        word = input().strip()
    except:
        break
    if word in dictionary:
        print(dictionary[word])
    else:
        print("eh")
