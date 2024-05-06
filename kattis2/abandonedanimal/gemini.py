# 5.1 Error 1/38
from collections import defaultdict

def main():
    # Read the number of stores and items
    n, k = map(int, input().split())

    # Read the inventory of each store
    inventory = defaultdict(set)
    for i in range(k):
        store, item = input().split()
        inventory[int(store)].add(item)

    # Read the list of items purchased
    m = int(input())
    purchases = [input() for _ in range(m)]

    # Check if it is possible to determine which store each item was purchased from
    possible = True
    store = 0
    for purchase in purchases:
        if purchase not in inventory[store]:
            possible = False
            break
        store = (store + 1) % n

    # Print the result
    if not possible:
        print("impossible")
    elif inventory[store] == set(purchases):
        print("unique")
    else:
        print("ambiguous")

if __name__ == "__main__":
    main()