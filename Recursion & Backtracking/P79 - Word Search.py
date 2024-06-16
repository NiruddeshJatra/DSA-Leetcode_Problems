"""
### Problem
Given a 2D board and a word, find if the word exists in the grid. The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

### Intuition
To determine if the word exists in the grid, we can use backtracking. For each cell in the grid, we start searching for the word. If the character matches the first character of the word, we recursively search for the next characters in the adjacent cells.

### Approach
1. **Base Case**: If the current index `k` matches the length of the word, it means we have found the word in the grid, so return `True`.
2. **Boundary Check**: If the current cell is out of the grid boundaries or the character does not match the current character of the word, return `False`.
3. **Backtracking Function**: Define a recursive function `backtrack` to search the word in the grid:
   - If the current index `k` matches the length of the word, return `True`.
   - Check the boundaries and character match conditions.
   - Temporarily mark the current cell as visited.
   - Recursively search for the next character in the adjacent cells (up, down, left, right).
   - If any of the recursive calls return `True`, the word exists in the grid, so return `True`.
   - Restore the current cell's value and return `False` if no path matches the word.
4. **Initialization**: Iterate over each cell in the grid and start the backtracking process.
5. **Return**: If the word is found, return `True`; otherwise, return `False`.

### Time Complexity
The time complexity is O(N * 3^L), where N is the number of cells in the board and L is the length of the word. Each cell can be a starting point and we have at most 3 directions to explore (excluding the direction we came from).

### Space Complexity
The space complexity is O(L) for the recursion stack, where L is the length of the word.

### Algorithm
1. Define the `backtrack` function:
   - Check if the current index `k` equals the length of the word and return `True`.
   - Check the boundaries and character match conditions.
   - Temporarily mark the current cell as visited.
   - Recursively call `backtrack` for adjacent cells.
   - Restore the current cell's value.
   - Return `False` if no path matches the word.
2. Iterate over each cell in the grid and start the backtracking process.
3. Return the result.
"""

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i, j, k):
            if k == len(word):
                return True
            if (
                i < 0
                or i == len(board)
                or j < 0
                or j == len(board[0])
                or board[i][j] != word[k]
            ):
                return False

            temp = board[i][j]
            board[i][j] = ""
            if (
                backtrack(i + 1, j, k + 1)
                or backtrack(i - 1, j, k + 1)
                or backtrack(i, j + 1, k + 1)
                or backtrack(i, j - 1, k + 1)
            ):
                return True

            board[i][j] = temp
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        return False
