# Time Complexity:
# - O(m*n), where m is the number of rows and n is the number of columns in the board.
# - We iterate through each cell twice, and for each cell, we check up to 8 neighboring cells.

# Space Complexity:
# - O(1), as we modify the board in-place without using additional data structures that scale with input size.
# - We only use a fixed amount of extra space for variables regardless of the board size.

# INTUITION:
# Conway's Game of Life requires us to update all cells simultaneously based on their neighbors.
# The challenge is that we can't update cells one by one because later updates would be based on
# already modified values, not the original state.
#
# Instead of using extra space to store the next state, we can use different values to represent
# both the current state and the next state in the same cell:
# - 0: Currently dead, stays dead
# - 1: Currently alive, stays alive
# - 2: Currently dead, will become alive
# - 3: Currently alive, will become dead
#
# For example, with the board:
# [
#   [0,1,0],
#   [0,0,1],
#   [1,1,1]
# ]
# After applying the rules and using our encoding:
# [
#   [0,0,0],
#   [1,0,1],
#   [0,1,1]
# ]

# ALGO:
# 1. Iterate through each cell in the board.
# 2. For each cell, count the number of live neighbors (cells with values 1 or 3).
# 3. Apply the Game of Life rules, using our encoding:
#    - If a dead cell (0) has exactly 3 live neighbors, it becomes alive (2).
#    - If a live cell (1) has fewer than 2 or more than 3 live neighbors, it dies (3).
# 4. After all cells are processed, convert the intermediate states to final states:
#    - 2 (dead->alive) becomes 1
#    - 3 (alive->dead) becomes 0

from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
            
        rowCount, colCount = len(board), len(board[0])
        # All 8 possible directions: horizontal, vertical, and diagonal
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        # First pass: Mark cells that will change state
        for row in range(rowCount):
            for col in range(colCount):
                liveNeighbors = 0
                
                # Count live neighbors (cells with value 1 or 3)
                for deltaRow, deltaCol in directions:
                    neighborRow, neighborCol = row + deltaRow, col + deltaCol
                    
                    # Check if the neighbor is within bounds and is alive (1) or was alive but will die (3)
                    if (0 <= neighborRow < rowCount and 
                        0 <= neighborCol < colCount and 
                        board[neighborRow][neighborCol] in [1, 3]):
                        liveNeighbors += 1
                
                # Apply Game of Life rules with our encoding
                if board[row][col] == 0:  # Currently dead cell
                    if liveNeighbors == 3:
                        # Rule 4: Dead cell with exactly 3 live neighbors becomes alive
                        board[row][col] = 2  # Mark as "will become alive"
                else:  # Currently live cell
                    if liveNeighbors < 2 or liveNeighbors > 3:
                        # Rule 1 & 3: Live cell with <2 or >3 live neighbors dies
                        board[row][col] = 3  # Mark as "will become dead"
        
        # Second pass: Update cells to their new states
        for row in range(rowCount):
            for col in range(colCount):
                if board[row][col] == 2:
                    # Dead cell that should become alive
                    board[row][col] = 1
                elif board[row][col] == 3:
                    # Live cell that should become dead
                    board[row][col] = 0
