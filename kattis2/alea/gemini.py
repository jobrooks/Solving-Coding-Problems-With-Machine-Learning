import sys
from typing import List, Tuple

def main():
    # Read input data
    scenarios = []  # type: List[Tuple[int, int, int]]
    for line in sys.stdin:
        A, C, X_0 = map(int, line.split())
        if A == C == X_0 == 0:
            break
        scenarios.append((A, C, X_0))

    # Solve each scenario
    for A, C, X_0 in scenarios:
        # Calculate roll sequence
        rolls = []  # type: List[int]
        X = X_0
        while len(rolls) < 11*5:
            X = (A * X + C) % (2**32)
            rolls.append((X >> 16) % 6 + 1)

        # Calculate score for each combination
        combinations = {
            "Ones": 0,
            "Twos": 0,
            "Threes": 0,
            "Fours": 0,
            "Fives": 0,
            "Sixes": 0,
            "Sequence": 0,
            "Full House": 0,
            "Four of a kind": 0,
            "Five of a kind": 0,
            "Chance": 0,
        }  # type: Dict[str, int]
        for i in range(11):
            dice = rolls[5*i:5*i+5]
            counts = {}  # type: Dict[int, int]
            for die in dice:
                counts[die] = counts.get(die, 0) + 1

            # Check for specific combinations
            if 1 in counts and counts[1] >= 1:
                combinations["Ones"] += counts[1]
            if 2 in counts and counts[2] >= 2:
                combinations["Twos"] += 2*counts[2]
            if 3 in counts and counts[3] >= 3:
                combinations["Threes"] += 3*counts[3]
            if 4 in counts and counts[4] >= 4:
                combinations["Fours"] += 4*counts[4]
            if 5 in counts and counts[5] >= 5:
                combinations["Fives"] += 5*counts[5]
            if 6 in counts and counts[6] >= 6:
                combinations["Sixes"] += 6*counts[6]
            if set(dice) == set([1, 2, 3, 4, 5]):
                combinations["Sequence"] = 30
            if len(set(counts.values())) == 2 and 3 in counts and 2 in counts:
                combinations["Full House"] = sum(dice)
            if len(set(counts.values())) == 2 and 4 in counts and 1 in counts:
                combinations["Four of a kind"] = sum(dice)
            if len(set(counts.values())) == 1:
                combinations["Five of a kind"] = 50
            combinations["Chance"] += sum(dice)

        # Print maximum score
        print(max(combinations.values()))

if __name__ == "__main__":
    main()