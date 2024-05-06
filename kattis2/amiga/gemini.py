from collections import defaultdict
from typing import List, Tuple, Dict

# The possible values for each fact type
NAMES = ["anna", "bernhard", "chris", "david", "ellen"]
NATIONALITIES = ["danish", "finnish", "icelandic", "norwegian", "swedish"]
COLORS = ["blue", "green", "red", "white", "yellow"]
COMPUTERS = ["amiga", "atari", "linux", "mac", "windows"]
LANGUAGES = ["c", "c++", "java", "pascal", "perl"]
FACT_TYPES = ["same-as", "left-of", "right-of", "next-to"]


def parse_facts(facts: List[str]) -> Dict[str, Dict[str, str]]:
    """
    Parses the facts and returns a dictionary of dictionaries.
    The outer dictionary keys are the fact types, and the inner dictionary keys are the names,
    nationalities, colors, computers, or languages.
    The inner dictionary values are the values associated with the keys.
    """
    fact_dict = defaultdict(dict)
    for fact in facts:
        fact_type, name1, name2 = fact.split()
        fact_dict[fact_type][name1] = name2
    return fact_dict


def is_consistent(fact_dict: Dict[str, Dict[str, str]]) -> bool:
    """
    Checks if the facts are consistent.

    Returns True if the facts are consistent, False otherwise.
    """

    # Check if there are any contradictions in the same-as facts
    for name, color in fact_dict["same-as"].items():
        if color in fact_dict["same-as"] and fact_dict["same-as"][color] != name:
            return False

    # Check if there are any contradictions in the left-of and right-of facts
    for name, room in fact_dict["left-of"].items():
        if room in fact_dict["right-of"] and fact_dict["right-of"][room] != name:
            return False

    # Check if there are any contradictions in the next-to facts
    for name1, name2 in fact_dict["next-to"].items():
        if name2 not in fact_dict["next-to"] or fact_dict["next-to"][name2] != name1:
            return False

    return True


def find_amiga_owner(fact_dict: Dict[str, Dict[str, str]]) -> str:
    """
    Finds the owner of the Amiga computer.

    Returns the name of the Amiga owner if found, or "cannot identify the amiga owner" otherwise.
    """
    # Find the room with the Amiga computer
    amiga_room = None
    for name, computer in fact_dict["same-as"].items():
        if computer == "amiga":
            amiga_room = name
            break

    if not amiga_room:
        return "cannot identify the amiga owner"

    # Find the person who lives in the Amiga room
    amiga_owner = None
    for name, room in fact_dict["same-as"].items():
        if room == amiga_room:
            amiga_owner = name
            break

    return f"{amiga_owner} owns the amiga"


def main():
    # Read the number of scenarios
    num_scenarios = int(input())

    # Process each scenario
    for scenario in range(1, num_scenarios + 1):
        # Read the number of facts
        num_facts = int(input())

        # Read the facts
        facts = []
        for _ in range(num_facts):
            facts.append(input())

        # Parse the facts
        fact_dict = parse_facts(facts)

        # Check if the facts are consistent
        if not is_consistent(fact_dict):
            print(f"scenario #{scenario}: impossible")
            continue

        # Find the owner of the Amiga computer
        amiga_owner = find_amiga_owner(fact_dict)
        print(f"scenario #{scenario}: {amiga_owner}")


if __name__ == "__main__":
    main()