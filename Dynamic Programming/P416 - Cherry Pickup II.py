# INTUITION (For Beginners):
# Imagine two robots starting at the top-left and top-right corners of a grid.
# Both robots want to collect the maximum number of cherries while moving to the bottom.
# They can move left, right, or down — and they shouldn't step out of bounds.
# The goal is to calculate the most cherries they can collect together.

# HOW DOES THIS SOLUTION WORK?
# 1. **State Definition:** `front[j1][j2]` stores the maximum cherries collected when robot1 is at column `j1` and robot2 at column `j2` in the current row.
# 2. **Initialization:** Start from the last row and move upwards.
# 3. **Transitions:** For each cell `(i, j1)` and `(i, j2)`:
#    - Pick cherries at both positions (if they’re not the same cell).
#    - Try all possible next moves (`-1`, `0`, `1`) for both robots.
#    - Take the maximum value from all possible next states.
# 4. **Result:** The final answer is the maximum cherries both robots can collect starting from the first row, with robot1 at column `0` and robot2 at column `n-1`.

# TIME COMPLEXITY:
# - O(m * n² * 9) → 3 possible moves for each robot, checking all combinations.

# SPACE COMPLEXITY:
# - O(n²) → We only keep two 2D arrays (`front` and `cur`).

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # `front` stores the results of the next row
        front = [[0] * (n + 1) for _ in range(n + 1)]

        # Initialize the last row
        for j1 in range(n):
            for j2 in range(n):
                front[j1][j2] = 0

        # Traverse rows from bottom to top
        for i in range(m - 1, -1, -1):
            # `cur` stores results for the current row
            cur = [[0] * (n + 1) for _ in range(n + 1)]
            for j1 in range(n):
                for j2 in range(n):
                    # Try all possible movements for both robots
                    for dj1 in [-1, 0, 1]:
                        for dj2 in [-1, 0, 1]:
                            # Collect cherries
                            value = grid[i][j1] if j1 == j2 else grid[i][j1] + grid[i][j2]
                            # Check if the next positions are within bounds
                            if 0 <= j1 + dj1 < n and 0 <= j2 + dj2 < n:
                                value += front[j1 + dj1][j2 + dj2]
                            # Store the best result
                            cur[j1][j2] = max(cur[j1][j2], value)

            # Update front for the next iteration
            front = cur

        # Return the max cherries collected from the top row
        return front[0][n - 1]
