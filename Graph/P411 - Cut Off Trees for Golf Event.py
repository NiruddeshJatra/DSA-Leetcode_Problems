# Time Complexity:
# - O(T * M * N), where T is the number of trees, and M, N are the dimensions of the forest grid.
# - We perform a BFS for each tree, which takes O(M * N) in the worst case.

# Space Complexity:
# - O(M * N), for the queue and visited set used in the BFS.

# INTUITION:
# The goal is to cut all the trees in the forest in increasing height order with the minimum steps required.
# We use a BFS to navigate the grid, as it finds the shortest path in an unweighted grid.
# By sorting the trees by height and calculating the shortest distance to each tree sequentially, we can accumulate the total steps.

# Example:
# forest = [[1, 2, 3], [0, 0, 4], [7, 6, 5]]
# Sorted tree order: [(2, 0, 1), (3, 0, 2), (4, 1, 2), (5, 2, 2), (6, 2, 1), (7, 2, 0)]
# Cut trees in order while calculating the minimum distance with BFS.

# ALGO:
# 1. Collect all tree positions with their heights.
# 2. Sort the trees by height.
# 3. Use BFS to find the shortest path to each tree, updating the current position after each step.
# 4. If any tree is unreachable, return -1.
# 5. Return the accumulated steps.

from typing import List
from collections import deque

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        def distance(curRow, curCol, destRow, destCol):
            queue = deque([[0, curRow, curCol]])
            visited = set()
            visited.add((curRow, curCol))

            while queue:
                step, x, y = queue.popleft()
                if x == destRow and y == destCol:
                    return step

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < rows
                        and 0 <= ny < cols
                        and (nx, ny) not in visited
                        and forest[nx][ny] != 0
                    ):
                        visited.add((nx, ny))
                        queue.append([step + 1, nx, ny])

            return -1

        treeOrder = []
        rows, cols = len(forest), len(forest[0])
        for i in range(rows):
            for j in range(cols):
                if forest[i][j] > 1:
                    treeOrder.append([forest[i][j], i, j])

        treeOrder.sort()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        totalSteps = 0
        curRow, curCol = 0, 0

        for height, destRow, destCol in treeOrder:
            step = distance(curRow, curCol, destRow, destCol)
            if step == -1:
                return -1

            totalSteps += step
            curRow, curCol = destRow, destCol

        return totalSteps
