# 1.4 accepted 14/14

blimps = [input() for _ in range(5)]
found = [i+1 for i, code in enumerate(blimps) if "FBI" in code]

if found:
    print(*found)
else:
    print("HE GOT AWAY!")
