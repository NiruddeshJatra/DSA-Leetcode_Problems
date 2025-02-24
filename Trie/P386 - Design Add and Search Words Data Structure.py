# Time Complexity:
# addWord:
# - O(N) where N is length of word
# - Each character requires constant time operations
#
# search:
# - O(N * 26^M) where N is word length and M is number of dots
# - Each dot can match 26 characters, creating branching paths
# - Worst case when searching "..." is O(26^N)

# Space Complexity:
# - O(N * W) where N is total length of all words and W is number of words
# - Each node stores children dictionary and boolean flag
# - DFS recursion stack is O(N) in worst case

# INTUITION:
# Use a trie (prefix tree) to store words efficiently.
# Each node represents a character and has:
# 1. Dictionary of child nodes for next characters
# 2. Boolean flag indicating if it's end of a word
#
# Special handling for '.' pattern:
# - Try all possible characters at that position
# - Use DFS to explore all matching paths
#
# Example:
# add("bad")
# add("dad")
# search("b.d") -> true
# search(".ad") -> true
# search("...") -> true

# ALGO:
# TrieNode structure:
# - children: dict mapping char to child nodes
# - isWord: boolean indicating word ending
#
# addWord:
# 1. Start from root
# 2. For each char:
#    - Create new node if char doesn't exist
#    - Move to child node
# 3. Mark last node as word end
#
# search:
# 1. Use DFS starting from root
# 2. For each char:
#    - If '.', try all children recursively
#    - Otherwise, follow matching child if exists
# 3. Return true if path reaches word end

class TrieNode:
   def __init__(self):
       self.children = {}  # Maps character to child node
       self.isWord = False # Marks end of word

class WordDictionary:
   def __init__(self):
       """
       Initialize your data structure here.
       """
       self.root = TrieNode()

   def addWord(self, word: str) -> None:
       """
       Adds a word into the data structure.
       """
       currentNode = self.root
       
       # Build path in trie for word
       for char in word:
           # Create new node if character doesn't exist
           if char not in currentNode.children:
               currentNode.children[char] = TrieNode()
           # Move to child node
           currentNode = currentNode.children[char]
           
       # Mark end of word
       currentNode.isWord = True

   def search(self, word: str) -> bool:
       """
       Returns if the word is in the data structure.
       A word could contain the dot character '.' to represent any letter.
       """
       def dfsSearch(node: TrieNode, index: int) -> bool:
           # Reached end of word
           if index == len(word):
               return node.isWord
           
           currentChar = word[index]
           
           # Handle wildcard
           if currentChar == '.':
               # Try all possible characters
               for childNode in node.children.values():
                   if dfsSearch(childNode, index + 1):
                       return True
               return False
           
           # Handle normal character
           if currentChar in node.children:
               return dfsSearch(node.children[currentChar], index + 1)
               
           return False
           
       return dfsSearch(self.root, 0)
