import sys

def solve(scenario):
    # Read the number of facts for this scenario.
    num_facts = int(sys.stdin.readline())

    # Create a dictionary to store the facts.
    facts = {}

    # Read the facts.
    for i in range(num_facts):
        line = sys.stdin.readline().split()
        facts[line[0]] = line[2]

    # Check if the input data is inconsistent.
    if inconsistent(facts):
        return "impossible"

    # Find the room number of the Amiga owner.
    room_number = find_room_number(facts)

    # Find the name of the Amiga owner.
    owner = find_owner(facts, room_number)

    # Return the result.
    return f"{owner} owns the amiga."

def inconsistent(facts):
    # Check if there are any contradictions in the facts.
    for fact1 in facts:
        for fact2 in facts:
            if fact1 == fact2:
                continue
            if facts[fact1] == facts[fact2] and fact1 != fact2:
                return True
    return False

def find_room_number(facts):
    # Find the room number of the Amiga owner.
    for fact in facts:
        if facts[fact] == "amiga":
            return int(fact)

def find_owner(facts, room_number):
    # Find the name of the Amiga owner.
    for fact in facts:
        if int(fact) == room_number:
            return facts[fact]

def main():
    # Read the number of scenarios.
    num_scenarios = int(sys.stdin.readline())

    # Solve each scenario.
    for i in range(num_scenarios):
        print(f"scenario #{i+1}:", solve(i+1))

if __name__ == "__main__":
    main()