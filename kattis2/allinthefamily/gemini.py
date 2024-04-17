import sys

def find_common_ancestor(person1, person2):
    """Finds the common ancestor of two people in a family tree."""
    # Get the list of ancestors of each person.
    ancestors1 = []
    ancestors2 = []
    current_person = person1
    while current_person != None:
        ancestors1.append(current_person)
        current_person = parent[current_person]
    current_person = person2
    while current_person != None:
        ancestors2.append(current_person)
        current_person = parent[current_person]
    
    # Find the first common ancestor.
    common_ancestor = None
    for ancestor1 in ancestors1:
        for ancestor2 in ancestors2:
            if ancestor1 == ancestor2:
                common_ancestor = ancestor1
                break
        if common_ancestor != None:
            break
    
    return common_ancestor

def get_relationship(person1, person2, common_ancestor):
    """Gets the relationship between two people in a family tree."""
    # Get the number of generations each person is removed from the common ancestor.
    generations1 = ancestors[person1].index(common_ancestor) + 1
    generations2 = ancestors[person2].index(common_ancestor) + 1
    
    # Determine the relationship based on the number of generations each person is removed.
    if generations1 == 0:
        if generations2 == 1:
            relationship = "child of"
        elif generations2 > 1:
            relationship = "great^{}-grandchild of".format(generations2 - 2)
    elif generations1 == generations2:
        if generations2 == 1:
            relationship = "sibling of"
        else:
            relationship = "{}th cousins".format(generations2 - 1)
    else:
        relationship = "{}th cousins, {} time{} removed".format(generations1 - 1, generations2 - generations1, "" if generations2 - generations1 == 1 else "s")
    
    return relationship

# Get the number of tree descriptions and the number of query pairs.
t, p = map(int, input().split())

# Create a dictionary to store the children of each person.
children = {}

# Read the tree descriptions.
for i in range(t):
    tree_description = input().split()
    person = tree_description[0]
    children[person] = tree_description[1:]

# Create a dictionary to store the ancestors of each person.
ancestors = {}

# Find the ancestors of each person.
for person in children:
    ancestors[person] = []
    current_person = person
    while current_person != None:
        ancestors[person].append(current_person)
        current_person = parent[current_person]

# Read the query pairs.
for i in range(p):
    pair = input().split()
    person1 = pair[0]
    person2 = pair[1]
    
    # Find the common ancestor of the two people.
    common_ancestor = find_common_ancestor(person1, person2)
    
    # Get the relationship between the two people.
    relationship = get_relationship(person1, person2, common_ancestor)
    
    # Print the relationship.
    print("{} {} {}".format(person1, relationship, person2))