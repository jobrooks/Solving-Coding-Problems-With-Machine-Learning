# 2.2 wrong answer 1/11

x = int(input())
queue = input()

# Initialize counts
w_count = 0
m_count = 0
skipped = 0

for person in queue:
    # If adding this person doesn't violate the limit, add them to the count
    if abs(w_count - m_count) <= x:
        if person == 'W':
            w_count += 1
        else:
            m_count += 1
    # Otherwise, skip this person and increment the skipped count
    else:
        skipped += 1

print(w_count + m_count - skipped)
