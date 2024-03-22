# 2.6 wrong answer 0/2

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    
    # Read the offers
    offers = []
    for i in range(n):
        a, b = map(int, input().split())
        if a <= m:
            offers.append((a, b))
    
    # Find the best offer
    best_offer = None
    for a, b in offers:
        num_tickets = m // a * a
        cost = (m // a) * b
        if num_tickets > 0 and (best_offer is None or cost < best_offer[1]):
            best_offer = (num_tickets, cost, b)
        elif num_tickets > 0 and cost == best_offer[1] and num_tickets > best_offer[0]:
            best_offer = (num_tickets, cost, b)
    
    # Print the result
    if best_offer is None:
        print("No suitable tickets offered")
    else:
        print("Buy {} tickets for ${}".format(best_offer[0], best_offer[1]))
