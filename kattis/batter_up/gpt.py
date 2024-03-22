# 1.4 accepted 20/20

n = int(input())
at_bats = list(map(int, input().split()))

num_official_at_bats = num_bases = 0

for at_bat in at_bats:
    if at_bat != -1:
        num_official_at_bats += 1
        num_bases += at_bat

slugging_percentage = num_bases / num_official_at_bats

print(slugging_percentage)
