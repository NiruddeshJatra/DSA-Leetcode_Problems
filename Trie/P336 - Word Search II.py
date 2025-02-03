# Time Complexity:
# - Building Trie: O(N*L) where N is number of words and L is average word length
# - DFS: O(M*N*4^L) where M,N are board dimensions, L is max word length
#   * Each cell has 4 directions
#   * Path can be up to L length
#   * Need to check every cell
# - Overall: O(N*L + M*N*4^L)

# Space Complexity:
# - Trie: O(N*L) for storing all words
# - Recursion stack: O(L) for DFS path length
# - Result set: O(N*L) to store found words
# - Overall: O(N*L)

# INTUITION:
# Combine Trie + DFS to efficiently search words:
# 1. Build Trie from word list for fast prefix lookup
# 2. DFS from each cell to find valid words
# 3. Mark visited cells to avoid cycles
# Example:
# board = [["o","a","a","n"],
#          ["e","t","a","e"],
#          ["i","h","k","r"],
#          ["i","f","l","v"]]
# words = ["oath","pea","eat","rain"]
# Start DFS from each cell, use Trie to prune invalid paths

# ALGO:
# 1. Build Trie from word list
# 2. For each cell in board:
#    Run DFS with backtracking:
#    a) Base cases:
#       - Out of bounds
#       - Cell not in Trie children
#    b) Mark cell as visited
#    c) Add to current word
#    d) If word exists in Trie, add to results
#    e) Recursive DFS in 4 directions
#    f) Restore cell (backtrack)
# 3. Return unique found words

def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
   def backtrackDFS(row: int, col: int, node: TrieNode, currentWord: str) -> None:
       # Check bounds and valid prefix
       if (row < 0 or 
           row == ROWS or 
           col < 0 or 
           col == COLS or
           board[row][col] not in node.children):
           return
           
       # Save current letter and mark as visited
       letter = board[row][col]
       board[row][col] = ""
       
       # Move to next node in Trie
       node = node.children[letter]
       currentWord += letter
       
       # Check if we found a word
       if node.isWord:
           foundWords.add(currentWord)
           
       # DFS in all 4 directions
       backtrackDFS(row + 1, col, node, currentWord)
       backtrackDFS(row - 1, col, node, currentWord)
       backtrackDFS(row, col + 1, node, currentWord)
       backtrackDFS(row, col - 1, node, currentWord)
       
       # Restore letter (backtrack)
       board[row][col] = letter
   
   # Build Trie
   root = TrieNode()
   for word in words:
       root.addWord(word)
   
   # Initialize variables
   ROWS, COLS = len(board), len(board[0])
   foundWords = set()
   
   # Start DFS from each cell
   for row in range(ROWS):
       for col in range(COLS):
           backtrackDFS(row, col, root, '')
           
   return list(foundWords)
