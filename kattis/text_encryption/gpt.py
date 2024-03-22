# 3.3 wrong answer 0/2
while True:
    n = int(input())
    if n == 0:
        break
    message = input().replace(" ", "").upper()
    ciphertext = ""
    for i in range(n):
        for j in range(i, len(message), n):
            ciphertext += message[j]
    print(ciphertext)
