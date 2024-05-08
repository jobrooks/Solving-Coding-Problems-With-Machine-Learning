import sys

sys.setrecursionlimit(10 ** 6)

def dfs(r, c, d):
    global ans, vis

    if r == r_g and c == c_g:
        if len(s) < len(ans) or (len(s) == len(ans) and s < ans):
            ans = s
        return

    if vis[r][c][d] == 1 or (r == r_u and c == c_u):
        return

    vis[r][c][d] = 1
    s += d
    dfs(r, c + 1, 'R')
    dfs(r, c - 1, 'L')
    dfs(r + 1, c, 'D')
    dfs(r - 1, c, 'U')
    s = s[:-1]
    vis[r][c][d] = 0

if __name__ == '__main__':
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break

        r_b, c_b = map(int, input().split())
        r_c, c_c = map(int, input().split())
        r_g, c_g = map(int, input().split())
        r_u, c_u = map(int, input().split())
        input()

        s = ''
        ans = 'ZZZZZZZZZZZZZZZZZZZZZ'
        vis = [[[0] * 4 for _ in range(m + 1)] for _ in range(n + 1)]
        dfs(r_b, c_b, 'R')
        dfs(r_b, c_b, 'L')
        dfs(r_b, c_b, 'D')
        dfs(r_b, c_b, 'U')

        if ans == 'ZZZZZZZZZZZZZZZZZZZZZ':
            print('NO')
        else:
            print('YES')
            print(ans)