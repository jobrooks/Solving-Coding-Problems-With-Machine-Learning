# 3.9 wrong answer 0/7
import sys

n, k = map(int, input().split())
players = []
for i in range(n**2):
    players.append(int(input()))

# Seed the tournament
tournament = []
num_players = 2**n
for i in range(n):
    round_players = []
    for j in range(num_players // 2):
        a = players[j + num_players // 2 * i]
        b = players[j + num_players // 2 * i + num_players // 2]
        round_players.append((a, b))
    tournament.append(round_players)
    num_players //= 2

# Simulate the tournament
close_games = 0
for round_players in tournament:
    close_games_round = 0
    for game in round_players:
        if abs(game[0] - game[1]) <= k:
            close_games_round += 1
    close_games += close_games_round
    if close_games_round == len(round_players):
        # All games were close, we are done
        break

print(close_games)
