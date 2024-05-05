from math import atan2

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def graham_scan(points):
    n = len(points)
    
    if n < 3:
        return None
    
    pivot = min(points, key=lambda point: (point[1], point[0]))
    
    sorted_points = sorted(points, key=lambda point: (atan2(point[1] - pivot[1], point[0] - pivot[0]), point))
    
    hull = [pivot, sorted_points[0], sorted_points[1]]
    
    for i in range(2, n):
        while len(hull) > 1 and orientation(hull[-2], hull[-1], sorted_points[i]) != 2:
            hull.pop()
        hull.append(sorted_points[i])
    
    return hull

points_set = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
convex_hull = graham_scan(points_set)

print("Convex Hull Points:")
for point in convex_hull:
    print(point)