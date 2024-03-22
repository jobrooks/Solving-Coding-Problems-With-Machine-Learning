# 3.2 wrong answer 0/20
n = int(input())
latest_packet_played = 0
total_lag_time = 0

for i in range(n):
    ti, packet_number = map(int, input().split())
    if packet_number == latest_packet_played + 1:
        # This packet can be played immediately
        latest_packet_played += 1
    else:
        # We need to wait for some earlier packet to be played first
        waiting_time = ti - packet_number - latest_packet_played
        if waiting_time > 0:
            total_lag_time += waiting_time
        latest_packet_played = packet_number - 1

print(total_lag_time)
