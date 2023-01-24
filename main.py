# Function to generate the array of points P
def generate_points(k):
    s = [290797]
    for i in range(1, 2*k+1):
        s.append((s[i-1] * s[i-1]) % 50515093)
    P = [(s[2*i], s[2*i+1]) for i in range(k)]
    return P

# Function to find the shortest distance between two points


def distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

# Divide and conquer function to find the shortest distance in the array of points


def shortest_distance(P, start, end):
    if end - start <= 3:
        # Base case: check all possible pairs of points
        min_dist = float('inf')
        for i in range(start, end):
            for j in range(i+1, end):
                dist = distance(P[i], P[j])
                if dist < min_dist:
                    min_dist = dist
        return min_dist
    else:
        # Divide the array of points into two halves
        mid = (start + end) // 2
        min_dist = min(shortest_distance(P, start, mid),
                       shortest_distance(P, mid, end))

        # Check for any points that are closer than min_dist within the two halves
        strip = []
        for i in range(start, end):
            if abs(P[i][0] - P[mid][0]) < min_dist:
                strip.append(P[i])

        # Sort the points in the strip by their y-coordinate
        strip.sort(key=lambda x: x[1])

        # Check for any points that are closer than min_dist in the strip
        for i in range(len(strip)):
            for j in range(i+1, min(i+7, len(strip))):
                dist = distance(strip[i], strip[j])
                if dist < min_dist:
                    min_dist = dist

        return min_dist


# Generate the array of points
P = generate_points(2000000)

# Find the shortest distance between any two distinct points
min_dist = shortest_distance(P, 0, len(P))
print("Shortest distance for k:", round(min_dist, 9))
