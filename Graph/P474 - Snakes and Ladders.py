# Time Complexity:
# - O(N^2), where N is the side length of the board (N x N).
# - In the worst case, we visit each of the N^2 squares once using BFS.
# - Each square is processed at most once due to the visited set.

# Space Complexity:
# - O(N^2), for the queue and visited set, which can store up to N^2 squares in the worst case.

# INTUITION:
# This is a shortest path problem where we want to find the minimum number of moves to reach
# the last square. BFS is perfect for finding the shortest path in unweighted graphs.
# 
# The key insight is to treat each square as a node in a graph, where edges connect squares
# that are reachable in one dice roll (1-6 steps). Snakes and ladders are teleportations
# that change our destination square.
# 
# We need to handle the board's numbering system: squares are numbered 1 to N^2 in a
# "boustrophedon" (zigzag) pattern. We reverse the board to make bottom-left square (1,1)
# correspond to array index [0,0]. For even rows we go left-to-right, for odd rows right-to-left.
# 
# Example: 6x6 board numbered 1-36, where 36 is top-right, 1 is bottom-left.
# After reversing: 1 is at [0,0], 6 is at [0,5], 7 is at [1,5], 12 is at [1,0].

# ALGO:
# 1. Reverse the board to handle the bottom-to-top numbering
# 2. Create helper function to convert square number to board coordinates
# 3. Use BFS starting from square 1 with 0 moves
# 4. For each square, try all possible dice rolls (1-6):
#    a. Calculate next square position
#    b. Check if there's a snake/ladder and update destination
#    c. If we reach the final square, return moves + 1
#    d. If square not visited, add to queue and mark as visited
# 5. Return -1 if no path found

from typing import List
from collections import deque

class Solution:
   def snakesAndLadders(self, board: List[List[int]]) -> int:
       boardSize = len(board)
       board.reverse()  # Reverse to handle bottom-to-top numbering

       def squareToCoordinates(squareNumber):
           row = (squareNumber - 1) // boardSize
           col = (squareNumber - 1) % boardSize
           # Handle zigzag pattern: odd rows go right-to-left
           if row % 2 == 1:
               col = boardSize - 1 - col
           return [row, col]

       bfsQueue = deque([[1, 0]])  # [current_square, moves_count]
       visitedSquares = set()

       while bfsQueue:
           currentSquare, movesCount = bfsQueue.popleft()
           
           # Try all possible dice rolls (1 to 6)
           for diceRoll in range(1, 7):
               nextSquare = currentSquare + diceRoll
               row, col = squareToCoordinates(nextSquare)
               
               # Check for snake or ladder
               if board[row][col] != -1:
                   nextSquare = board[row][col]
               
               # Check if we reached the final square
               if nextSquare == boardSize * boardSize:
                   return movesCount + 1
               
               # Add to queue if not visited
               if nextSquare not in visitedSquares:
                   visitedSquares.add(nextSquare)
                   bfsQueue.append([nextSquare, movesCount + 1])

       return -1  # No path found
