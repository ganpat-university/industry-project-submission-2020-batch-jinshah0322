import heapq

def connectSticks(sticks):
    heapq.heapify(sticks)
    cost = 0

    while len(sticks) > 1:
        stick1 = heapq.heappop(sticks)
        stick2 = heapq.heappop(sticks)
        combined = stick1 + stick2
        cost += combined
        heapq.heappush(sticks, combined)

    return cost

sticks = [2, 4, 3]
min_cost = connectSticks(sticks)
print("Minimum Cost to Connect Sticks:", min_cost)
