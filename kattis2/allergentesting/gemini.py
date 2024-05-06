import math

def main():
    t = int(input())
    for _ in range(t):
        n, d = map(int, input().split())
        res = math.ceil(math.log2(n) * (d + 1))
        print(res)

if __name__ == "__main__":
    main()