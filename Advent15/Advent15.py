import heapq
import numpy as np


def dijkstra(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # down, right, up, left

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    min_heap = [(grid[0][0], 0, 0)]  # (total risk, x, y)
    visited = set()

    while min_heap:
        risk, x, y = heapq.heappop(min_heap)

        if (x, y) in visited:
            continue

        visited.add((x, y))

        if x == rows - 1 and y == cols - 1:
            return risk

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y):
                heapq.heappush(min_heap, (risk + grid[new_x][new_y], new_x, new_y))

    # If no path is found
    return None


# Input file name
input_file = "input.txt"

# Output file name
output_file = "output.txt"

# Read the content from the input file
with open(input_file, "r") as infile:
    content = infile.read().strip()

# Insert a comma between each number in each row
formatted_content = "\n".join(
    [
        ",".join(line[i : i + 1] for i in range(0, len(line), 1))
        for line in content.split("\n")
    ]
)

# Write the formatted content to the output file
with open(output_file, "w") as outfile:
    outfile.write(formatted_content)

print(f"Formatted content has been written to {output_file}")

#
# Read the content from the output file
with open(output_file, "r") as outfile:
    lines = outfile.read().strip().split("\n")

# Create a 2D array (grid) from the lines
grid = [list(map(int, line.split(","))) for line in lines]

# Print the resulting grid
for row in grid:
    print(row)
#

# Get the startpoint
start_point_integer = [grid[0][0]]
print("First integers:", start_point_integer)

result = dijkstra(grid)
print("Lowest risk:", result - start_point_integer[0])
