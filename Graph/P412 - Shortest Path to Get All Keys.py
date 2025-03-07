# INTUITION (Simple Explanation for Beginners):
# Imagine you're in a maze, and you need to collect all the keys to unlock doors and escape. 
# Keys are labeled as 'a', 'b', 'c', etc., and doors as 'A', 'B', 'C'. 
# You can only open a door if you have its corresponding key. Your goal is to find the shortest 
# path to collect all the keys. 
# We solve this problem using Breadth-First Search (BFS), which explores all possible paths step by step.

# HOW DOES THE SOLUTION WORK?
# 1. **Finding the Start and Keys:** We scan the grid to find the starting point ('@') and record which keys exist.
# 2. **BFS Setup:** We start BFS from the initial position, keeping track of the keys we’ve collected.
# 3. **Exploring Neighbors:** For each cell, we:
#    - **Move to Empty Cells ('.') or the Start ('@'):** If it’s a walkable cell, we move.
#    - **Pick Up Keys (a, b, c...):** If we find a key, we add it to our key collection.
#    - **Unlock Doors (A, B, C...):** If we reach a door, we only pass through if we have the corresponding key.
# 4. **Checking for Success:** If we collect all the keys, we return the number of steps taken.
# 5. **Handling Impossible Cases:** If we exhaust all possibilities without collecting every key, we return -1.

# TIME COMPLEXITY:
# - O(m * n * 2^k), where m and n are the grid dimensions, and k is the number of keys.
#   We explore each cell with every possible combination of collected keys.

# SPACE COMPLEXITY:
# - O(m * n * 2^k) for the visited set, storing positions and key states.

from typing import List

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        all_keys = [0] * 6
        start = None

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    start = (i, j)
                elif grid[i][j].islower():
                    all_keys[ord(grid[i][j]) - ord('a')] = 1

        all_keys = tuple(all_keys)
        if sum(all_keys) == 0:
            return 0

        from collections import deque
        visited = set()
        q = deque()
        initial_keys = tuple([0] * 6)
        q.append((start[0], start[1], initial_keys))
        visited.add((start[0], start[1], initial_keys))
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        moves = 0

        while q:
            for _ in range(len(q)):
                x, y, keys = q.popleft()
                for dx, dy in dirs:
                    r, c = x + dx, y + dy
                    if 0 <= r < m and 0 <= c < n and grid[r][c] != '#':
                        cell = grid[r][c]
                        new_keys = list(keys)
                        if cell.islower():
                            idx = ord(cell) - ord('a')
                            if new_keys[idx] == 0:
                                new_keys[idx] = 1
                        if cell.isupper():
                            idx = ord(cell.lower()) - ord('a')
                            if new_keys[idx] == 0:
                                continue  # No key, can't pass
                        new_keys_tup = tuple(new_keys)
                        if (r, c, new_keys_tup) in visited:
                            continue
                        if new_keys_tup == all_keys:
                            return moves + 1
                        visited.add((r, c, new_keys_tup))
                        q.append((r, c, new_keys_tup))
            moves += 1
        return -1
