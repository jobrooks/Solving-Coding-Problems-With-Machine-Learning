# 4.3 time limit exceeded 32/35

# read input
prev_animal = input()
n = int(input())
animals = [input() for _ in range(n)]

# find the possible animals to play
possible_animals = [animal for animal in animals if animal[0] == prev_animal[-1] and animal != prev_animal]

# check if there is an animal that eliminates the next player
eliminate_animals = [animal for animal in possible_animals if animal[-1] not in [other_animal[0] for other_animal in animals if other_animal != prev_animal and other_animal != animal]]

# output the result
if eliminate_animals:
    print(eliminate_animals[0] + "!")
elif possible_animals:
    print(possible_animals[0])
else:
    print("?")
