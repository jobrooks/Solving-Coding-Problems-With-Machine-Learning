# 5.1 Error 1/38
from collections import defaultdict

def main():
    # Read the number of stores and the number of items available
    N, K = map(int, input().split())

    # Read the items available at each store
    items_at_stores = defaultdict(list)
    for _ in range(K):
        i, S = input().split()
        i = int(i)
        items_at_stores[i].append(S)

    # Read the list of items purchased
    M = int(input())
    items_purchased = []
    for _ in range(M):
        items_purchased.append(input())

    # Find the stores where each item was purchased
    item_to_store = {}
    for item in items_purchased:
        for store in range(N):
            if item in items_at_stores[store]:
                item_to_store[item] = store
                break

    # Check if there is a unique path through the stores that matches the description
    stores_visited = set()
    for item in items_purchased:
        store = item_to_store[item]
        if store in stores_visited:
            return "ambiguous"
        else:
            stores_visited.add(store)

    if len(stores_visited) == N:
        return "unique"
    else:
        return "impossible"

if __name__ == "__main__":
    print(main())