while n != 0 or t != 0:
    e = (1 - t) / 2 + t  # expected fraction of correct answer
    c = e * 2 * c  # expected prize
    print("{:.3f}".format(c))  # round result to 3 fractional digits