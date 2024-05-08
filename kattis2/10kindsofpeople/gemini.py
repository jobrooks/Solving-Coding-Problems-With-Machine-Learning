# 4.6 Error 1/25
def valid_move(map, r, c, r_end, c_end):
    if r < 0 or r >= len(map):
        return False
    if c < 0 or c >= len(map[0]):
        return False
    if map[r][c] != '0':  # Decimal region
        if r == r_end and c == c_end:
            return True
        else:
            return False
    else:  # Binary region
        if map[r_end][c_end] == '0':
            if r == r_end and c == c_end:
                return True
            if r - 1 >= 0 and map[r - 1][c] == '0':
                return valid_move(map, r - 1, c, r_end, c_end)
            if r + 1 < len(map) and map[r + 1][c] == '0':
                return valid_move(map, r + 1, c, r_end, c_end)
            if c - 1 >= 0 and map[r][c - 1] == '0':
                return valid_move(map, r, c - 1, r_end, c_end)
            if c + 1 < len(map[0]) and map[r][c + 1] == '0':
                return valid_move(map, r, c + 1, r_end, c_end)
        return False


r, c = map(int, input().split())
map = [input() for _ in range(r)]
n = int(input())
for _ in range(n):
    r1, c1, r2, c2 = map(int, input().split())
    r1 -= 1
    c1 -= 1
    r2 -= 1
    c2 -= 1
    if map[r1][c1] == '0':
        if valid_move(map, r1, c1, r2, c2):
            print('binary')
        else:
            print('neither')
    else:
        if valid_move(map, r1, c1, r2, c2):
            print('decimal')
        else:
            print('neither')