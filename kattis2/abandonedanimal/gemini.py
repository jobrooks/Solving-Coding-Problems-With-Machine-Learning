from collections import defaultdict

def main():
    n_stores = int(input())
    n_items = int(input())
    stores = defaultdict(list)
    for _ in range(n_items):
        store, item = input().split()
        store = int(store)
        stores[store].append(item)

    n_purchases = int(input())
    purchases = []
    for _ in range(n_purchases):
        purchases.append(input())

    breadcrumbs = [None] * len(purchases)
    for i in range(len(purchases)):
        purchase = purchases[i]
        for j in range(len(stores)):
            if purchase in stores[j]:
                breadcrumbs[i] = j
                break

    if None in breadcrumbs:
        print("impossible")
    elif len(set(breadcrumbs)) == len(breadcrumbs):
        print("unique")
    else:
        print("ambiguous")

if __name__ == "__main__":
    main()