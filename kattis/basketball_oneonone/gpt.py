# 1.6 wrong answer 0/16

game_record = input()  # read the game record as input

# keep track of the score for each player
score_A, score_B = 0, 0

# process the game record one character at a time
for i in range(0, len(game_record), 2):
    # get the player and the number of points they scored
    player = game_record[i]
    points = int(game_record[i+1])

    # update the score for the player
    if player == 'A':
        score_A += points
    else:
        score_B += points

    # check if the game is over
    if score_A >= 11 or score_B >= 11:
        # check if the win-by-2 rule applies
        if abs(score_A - score_B) >= 2:
            # the player with the higher score wins
            if score_A > score_B:
                print('A')
            else:
                print('B')
            break

# if we get to the end of the game record and no winner has been determined,
# the player with the higher score wins
if score_A > score_B:
    print('A')
else:
    print('B')