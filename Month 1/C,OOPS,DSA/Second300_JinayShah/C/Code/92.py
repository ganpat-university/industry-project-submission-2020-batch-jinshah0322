import heapq

def maxPerformance(n, speed, efficiency, k):
    engineers = list(zip(efficiency, speed))
    engineers.sort(reverse=True)  

    min_heap = []  
    speed_sum, max_performance = 0, 0

    for eff, spd in engineers:
        heapq.heappush(min_heap, spd)
        speed_sum += spd

        if len(min_heap) > k - 1:
            speed_sum -= heapq.heappop(min_heap)

        max_performance = max(max_performance, speed_sum * eff)

    return max_performance % (10**9 + 7)

n = 6
speed = [2, 10, 3, 1, 5, 8]
efficiency = [5, 4, 3, 9, 7, 2]
k = 3
result = maxPerformance(n, speed, efficiency, k)
print("Maximum Performance of a Team:", result)
