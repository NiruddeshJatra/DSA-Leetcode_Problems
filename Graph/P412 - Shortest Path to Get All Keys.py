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
        allKeys = [0] * 6

        # Step 1: Find the start position and available keys
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    startRow, startCol = i, j
                elif grid[i][j].islower():
                    allKeys[ord(grid[i][j]) - ord('a')] = 1

        # Step 2: Convert the key list to a tuple (for hashable state tracking)
        allKeys = tuple(allKeys)
        curLevel = [(startRow, startCol, tuple([0] * 6))]
        visited = {(startRow, startCol, tuple([0] * 6))}
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)] 
        moves = 0

        # Step 3: Perform BFS
        while curLevel:
            nextLevel = []   
            for x, y, curKeys in curLevel:
                for dx, dy in dirs:
                    r, c = x + dx, y + dy

                    # Step 4: Check valid positions
                    if 0 <= r < m and 0 <= c < n and grid[r][c] != '#':
                        # 4.1: Empty cell or start position
                        if grid[r][c] in '.@':
                            if (r, c, curKeys) not in visited:
                                visited.add((r, c, curKeys))
                                nextLevel.append((r, c, curKeys))

                        # 4.2: Found a key
                        elif grid[r][c].islower():
                            newKeys = list(curKeys)
                            newKeys[ord(grid[r][c]) - ord('a')] = 1
                            newKeys = tuple(newKeys)

                            # Check if we collected all keys
                            if newKeys == allKeys:
                                return moves + 1

                            if (r, c, newKeys) not in visited:
                                visited.add((r, c, newKeys))
                                nextLevel.append((r, c, newKeys))

                        # 4.3: Found a door, check if we have the key
                        else:
                            if curKeys[ord(grid[r][c].lower()) - ord('a')] == 1 and (r, c, curKeys) not in visited:
                                visited.add((r, c, curKeys))
                                nextLevel.append((r, c, curKeys))

            # Step 5: Update for next level and increment moves
            curLevel = nextLevel           
            moves += 1

        # Step 6: No valid path to collect all keys
        return -1
