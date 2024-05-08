import sys

def main():
    n, s = map(int, sys.stdin.readline().split())
    cards = list(map(int, sys.stdin.readline().split()))
    for i in range(n):
        for j in range(n):
            if cards[i] + cards[j] == s:
                print("YES")
                return
            rev_i = int(str(cards[i])[::-1])
            rev_j = int(str(cards[j])[::-1])
            if cards[i] + rev_j == s or rev_i + cards[j] == s:
                print("YES")
                return
    print("NO")

if __name__ == "__main__":
    main()