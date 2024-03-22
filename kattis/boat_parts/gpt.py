# 1.6 accepted 12/12

p, n = map(int, input().split())
parts = set()
last_replacement = None

for day in range(1, n+1):
    part = input().strip()
    parts.add(part)
    
    if len(parts) == p:
        last_replacement = day
        break
        
if last_replacement is not None:
    print(last_replacement)
else:
    print("paradox avoided")
