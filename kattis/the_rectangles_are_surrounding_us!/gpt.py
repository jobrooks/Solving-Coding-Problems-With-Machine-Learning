# 2.8 accepted 13/13
def main():
    while True:
        n = int(input().strip())
        if n == 0:
            break
        grid = [[0 for _ in range(505)] for _ in range(505)]
        for _ in range(n):
            a, b, c, d = map(int, input().strip().split())
            for i in range(a, c):
                for j in range(b, d):
                    grid[i][j] = 1
        count = 0
        for i in range(505):
            for j in range(505):
                if grid[i][j] == 1:
                    count += 1
        print(count)

if __name__ == '__main__':
    main()
