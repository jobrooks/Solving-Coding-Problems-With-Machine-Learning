# 1.3 accepted 13/13

long_name = input().split("-")
short_name = ""

for name in long_name:
    short_name += name[0]

print(short_name)
