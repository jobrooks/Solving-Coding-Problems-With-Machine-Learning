import sys

class Person:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []

def find_common_ancestor(p1, p2):
    ancestors = set()
    while p1:
        ancestors.add(p1)
        p1 = p1.parent
    while p2:
        if p2 in ancestors:
            return p2
        p2 = p2.parent
    return None

def find_relationship(p1, p2):
    common_ancestor = find_common_ancestor(p1, p2)
    if not common_ancestor:
        return "No relationship"

    gen1 = 0
    while p1 != common_ancestor:
        p1 = p1.parent
        gen1 += 1

    gen2 = 0
    while p2 != common_ancestor:
        p2 = p2.parent
        gen2 += 1

    if gen1 == 0:
        if gen2 == 1:
            return "{} is the child of {}".format(p2.name, p1.name)
        else:
            return "{} is the great{} grandchild of {}".format(p2.name, ordinal(gen2 - 2), p1.name)

    if gen1 == gen2:
        if gen1 == 1:
            return "{} and {} are siblings".format(p1.name, p2.name)
        else:
            return "{} and {} are {} cousins".format(p1.name, p2.name, ordinal(gen1 - 1))

    if gen1 < gen2:
        gen1, gen2 = gen2, gen1
        p1, p2 = p2, p1

    return "{} and {} are {} cousins, {} time{} removed".format(p1.name, p2.name, ordinal(gen1 - 1), gen2 - gen1, "s" if gen2 - gen1 > 1 else "")

def ordinal(n):
    if n in (11, 12, 13):
        return "{}th".format(n)
    elif n % 10 == 1:
        return "{}st".format(n)
    elif n % 10 == 2:
        return "{}nd".format(n)
    elif n % 10 == 3:
        return "{}rd".format(n)
    else:
        return "{}th".format(n)

def main():
    t, p = map(int, sys.stdin.readline().strip().split())

    people = {}

    for i in range(t):
        line = sys.stdin.readline().strip().split()
        parent = people.get(line[0])
        for child in line[1:]:
            people[child] = Person(child, parent)
            if parent:
                parent.children.append(people[child])

    for i in range(p):
        line = sys.stdin.readline().strip().split()
        p1 = people[line[0]]
        p2 = people[line[1]]
        print(find_relationship(p1, p2))

if __name__ == "__main__":
    main()