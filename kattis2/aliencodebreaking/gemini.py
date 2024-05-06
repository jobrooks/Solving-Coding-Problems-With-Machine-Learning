def f(x):
    return (33 * x + 1) % (2**20)

def powf(x, p):
    if p == 0:
        return x
    return f(powf(x, p - 1))

def make_grid(x):
    grid = []
    for i in range(x):
        row = [powf(0, i + x * j) for j in range(x)]
        grid.append(row)
    return grid

def get_sums(grid):
    sums = [0] * len(grid)
    for i in range(len(grid)):
        for j in range(len(grid)):
            sums[i] += grid[j][i]
        sums[i] = sums[i] % (2**20)
    return sums

def to_base_ten(nums):
    num = 0
    for num_to_add, power in zip(nums, range(len(nums) - 1, -1, -1)):
        num += num_to_add * (10 ** power)
    return num

def to_base_27(num):
    result = ""
    while num > 0:
        result += str(num % 27)
        num //= 27
    return result

def shift(encrypted, pad):
    decrypted = ""
    for i, char in enumerate(encrypted):
        if char == " ":
            decrypted += " "
        else:
            decrypted += chr((ord(char) - 65 + int(pad[i])) % 27 + 65)
    return decrypted

if __name__ == "__main__":
    n, x = map(int, input().split())
    encrypted = input()
    grid = make_grid(x)
    sums = get_sums(grid)
    base_ten_num = to_base_ten(sums)
    base_27_pad = to_base_27(base_ten_num)
    decrypted = shift(encrypted, base_27_pad)
    print(decrypted)