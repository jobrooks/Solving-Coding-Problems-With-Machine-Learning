# 5.1 Time Limit Exception 0/38
n = int(input())
initial = input()
target = input()

# convert hat colors to integers for easier comparison
initial = [int(h == 'B') for h in initial]
target = [int(h == 'B') for h in target]

while True:
    # check if we reached the target configuration
    if initial == target:
        print("yes")
        break
    
    # check if no more changes are possible
    if initial == initial[::-1]:
        print("no")
        break
    
    # iterate through each mathemagician
    for i in range(n):
        left_neighbor = (i - 1 + n) % n
        right_neighbor = (i + 1) % n
        
        # check if the mathemagician needs to cast a charm
        if initial[i] != initial[left_neighbor] and initial[i] != initial[right_neighbor]:
            print("no")
            break
        
        # cast a charm to match the hat of a neighbor
        if initial[i] != initial[left_neighbor]:
            initial[i] = initial[left_neighbor]
        elif initial[i] != initial[right_neighbor]:
            initial[i] = initial[right_neighbor]
    
    # if the loop ended normally, continue to the next iteration
    else:
        continue
    
    # if we broke out of the loop, exit the
