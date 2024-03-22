# 1.8 accepted 33/33

n = int(input())
count = 1

for num in input().split():
    if num == "mumble":
        count += 1
    elif int(num) == count:
        count += 1
    else:
        print("something is fishy")
        break
else:
    print("makes sense")
