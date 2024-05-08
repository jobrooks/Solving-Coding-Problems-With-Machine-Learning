# 4.2 Error 1/58
def mod_pow(base, power, mod):
    if power == 0:
        return 1
    if power == 1:
        return base
    val = mod_pow(base, power // 2, mod)
    val = (val * val) % mod
    if power % 2 != 0:
        val = (val * base) % mod
    return val % mod


def solve(r: int, c: int) -> int:
    mod = int(1e9) + 7
    if r == 1 or c == 1:
        return 3
    if r == 2 and c == 2:
        return 6
    if r == 2:
        return mod_pow(6, c, mod)
    if c == 2:
        return mod_pow(6, r, mod)
    return (mod_pow(6, r, mod) * mod_pow(6, c, mod)) % mod


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        r, c = map(int, input().split())
        result = solve(r, c)
        print(result)