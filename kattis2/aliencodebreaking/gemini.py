def f(x):
    return (33 * x + 1) % (2 ** 20)


def fill_grid(X, N):
    grid = [[0] * X for _ in range(X)]
    for i in range(X):
        for j in range(X):
            grid[i][j] = (f ** (i + j + 1))(0)
    return grid


def get_column_sums(grid, X):
    column_sums = [0] * X
    for j in range(X):
        for i in range(X):
            column_sums[j] += grid[i][j]
    return column_sums


def get_pad(column_sums):
    pad = ""
    for sum in column_sums:
        pad += str(sum % (2 ** 20))
    return pad


def shift_message(encrypted_message, pad):
    decrypted_message = ""
    pad_index = 0
    for char in encrypted_message:
        if char == " ":
            decrypted_message += " "
            pad_index += 1
        else:
            decrypted_message += chr(
                ord(char) - int(pad[pad_index]) % 27
            )
            pad_index += 1
    return decrypted_message


def main():
    N, X = map(int, input().split())
    encrypted_message = input()
    grid = fill_grid(X, N)
    column_sums = get_column_sums(grid, X)
    pad = get_pad(column_sums)
    decrypted_message = shift_message(encrypted_message, pad)
    print(decrypted_message)


if __name__ == "__main__":
    main()