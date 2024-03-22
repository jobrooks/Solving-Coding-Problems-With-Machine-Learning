# 1.4 accepted 41/41

name = input()

compact_name = ""
prev_char = ""

for char in name:
    if char != prev_char:
        compact_name += char
    prev_char = char

print(compact_name)
