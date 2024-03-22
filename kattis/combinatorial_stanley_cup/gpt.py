# 3.1 accepted 20/20

n = int(input())
binary_n = bin(n)[2:]
num_ones = sum(1 for bit in binary_n if bit == '1')
num_odd = 2 ** num_ones
print(num_odd)
