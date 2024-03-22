# 1.8 accepted 2/2

while True:
    n = int(input())
    if n == 0:
        break
    
    menu = {}
    for i in range(n):
        line = input().split()
        name = line[0]
        items = line[1:]
        
        for item in items:
            if item not in menu:
                menu[item] = set()
            menu[item].add(name)
            
    for item in sorted(menu.keys()):
        print(item, ' '.join(sorted(menu[item])))
    
    print()
