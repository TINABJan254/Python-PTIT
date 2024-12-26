from itertools import combinations
import sys
import math

input = sys.stdin.read
data = input().split()

idx = 0
T = int(data[idx])
idx += 1
results = []

for _ in range(T):
    N = int(data[idx])
    idx += 1
    K = int(data[idx])
    idx += 1
    points = []
    for __ in range(N):
        x, y = int(data[idx]), int(data[idx+1])
        idx += 2
        points.append((x, y))
    
    found = False
    # Check all combinations of three points
    for a, b, c in combinations(points, 3):
        # Calculate the circumcircle center and radius
        A, B, C = a, b, c
        # Using determinant to find circumcenter
        D = 2 * (A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1]))
        if D == 0:
            continue  # Points are collinear, no valid circle
        ux = ((A[0]**2 + A[1]**2) * (B[1] - C[1]) + (B[0]**2 + B[1]**2) * (C[1] - A[1]) + (C[0]**2 + C[1]**2) * (A[1] - B[1])) / D
        uy = ((A[0]**2 + A[1]**2) * (C[0] - B[0]) + (B[0]**2 + B[1]**2) * (A[0] - C[0]) + (C[0]**2 + C[1]**2) * (B[0] - A[0])) / D
        r_squared = ((A[0] - ux)**2 + (A[1] - uy)**2)
        
        # Count points inside the circle
        inside_count = 0
        for p in points:
            dist_squared = (p[0] - ux)**2 + (p[1] - uy)**2
            if dist_squared < r_squared:
                inside_count += 1

        if inside_count == K:
            results.append("YES")
            found = True
            break

    if not found:
        results.append("NO")

for result in results:
    print(result)
