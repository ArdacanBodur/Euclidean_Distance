import math

"""I developed a function that calculates the minimum Euclidean value between two points.
In short, the working logic is to find the minimum distance between the two values ​​with the Euclidean distance formula."""

def mindistance(point1, point2):
    # point1: First point as (x1, y1)
    # point2: Second point as (x2, y2)
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) # Math op.

example_points = [(1, 2), (4, 6), (7, 1), (3, 3)]
distances = [] # Distances between points will be contained here!

for i in range(len(example_points)):
    for j in range(i + 1, len(example_points)):
        distance = mindistance(example_points[i], example_points[j])
        distances.append(distance)

print("All distances:", distances) # Prints all distances!

minimum_distance = min(distances) # We are taking the min. value.
print("Minimum distance:", minimum_distance) # Prints min. distances!
