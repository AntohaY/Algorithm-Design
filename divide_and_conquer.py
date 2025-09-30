import math
import sys

# --- Your merge sort, modified to accept a key function ---
def merge_sort(arr, key=lambda x: x):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid], key)
    right_half = merge_sort(arr[mid:], key)

    return merge(left_half, right_half, key)

def merge(left, right, key):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# --- Closest pair using divide and conquer ---
def closest_pair(points):
    # Sort by x using your merge_sort
    points = merge_sort(points, key=lambda p: p[0])
    return _closest_rec(points)

def _closest_rec(points):
    n = len(points)
    if n <= 3:
        # Brute-force for small groups
        min_dist = float("inf")
        pair = None
        for i in range(n):
            for j in range(i+1, n):
                dist = math.dist(points[i], points[j])
                if dist < min_dist:
                    min_dist = dist
                    pair = (points[i], points[j])
        return pair, min_dist

    mid = n // 2
    mid_x = points[mid][0]
    left_pair, left_dist = _closest_rec(points[:mid])
    right_pair, right_dist = _closest_rec(points[mid:])

    # Find best from left or right
    if left_dist < right_dist:
        d = left_dist
        best_pair = left_pair
    else:
        d = right_dist
        best_pair = right_pair

    # Build strip: points within d of mid_x
    strip = [p for p in points if abs(p[0] - mid_x) < d]
    # Sort strip by y-coordinate using your merge_sort
    strip = merge_sort(strip, key=lambda p: p[1])

    # Check neighbors in strip
    for i in range(len(strip)):
        # Check next up to 15 points ()
        for j in range(i+1, min(i+15, len(strip))):
            dist = math.dist(strip[i], strip[j])
            if dist < d:
                d = dist
                best_pair = (strip[i], strip[j])

    return best_pair, d

# --- Main function ---
def closepair():
    n = int(sys.stdin.readline().strip())
    points = [tuple(map(float, sys.stdin.readline().split())) for _ in range(n)]
    pair, dist = closest_pair(points)
    if pair:
        a, b = pair
        print(*a)  # print first point without parentheses
        print(*b)  # print second point

if __name__ == "__main__":
    closepair()
