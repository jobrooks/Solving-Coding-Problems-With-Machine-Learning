import sys

def main():
    # Read input
    previous_animal = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    unused_animals = []
    for _ in range(n):
        animal = sys.stdin.readline().strip()
        unused_animals.append(animal)

    # Check if there are any valid animal names
    valid_animals = []
    for animal in unused_animals:
        if animal[0] == previous_animal[-1]:
            valid_animals.append(animal)

    # Check if there are any animal names that eliminate the next player
    eliminating_animals = []
    for animal in valid_animals:
        if animal[-1] not in [x[-1] for x in unused_animals]:
            eliminating_animals.append(animal)

    # Print output
    if eliminating_animals:
        print(eliminating_animals[0] + "!")
    elif valid_animals:
        print(valid_animals[0])
    else:
        print("?")

if __name__ == "__main__":
    main()