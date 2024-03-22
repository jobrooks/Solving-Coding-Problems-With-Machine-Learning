# 2.9 wrong answer 0/19
import sys

def mech_counter_moves(monster_moves: str) -> str:
    counter_moves = ''
    combo_count = 0
    for move in monster_moves:
        if move == 'R':
            counter_moves += 'S'
        elif move == 'B':
            counter_moves += 'K'
        elif move == 'L':
            counter_moves += 'H'
        combo_count += 1
        if combo_count == 3:
            counter_moves += 'C'
            combo_count = 0
    return counter_moves

for line in sys.stdin.readlines():
  print(mech_counter_moves(line))