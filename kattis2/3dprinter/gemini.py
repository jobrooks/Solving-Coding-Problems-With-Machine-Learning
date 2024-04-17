n = int(input())
days = 1
printers = 1
while printers < n:
    printers = printers * 2
    days += 1
print(days)