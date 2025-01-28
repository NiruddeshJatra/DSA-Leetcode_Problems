# Time Complexity:
# - Insert: O(L), where L is length of word being inserted
# - Search: O(L), where L is length of word being searched
# - StartsWith: O(L), where L is length of prefix
# Each operation requires traversing characters of input string

# Space Complexity:
# - O(N * L), where N is total number of words and L is average word length
# - Each node in trie can have up to 26 children (lowercase English letters)

# INTUITION:
# Use a trie (prefix tree) to efficiently store and search strings.
# Each node represents a character and contains:
# - Dictionary of child nodes (next characters)
# - Boolean indicating if it's end of a word

# ALGO:
# Insert:
# 1. Start at root, traverse word characters
# 2. Create new nodes for missing characters
# 3. Mark last node as word end

# Search:
# 1. Start at root, traverse word characters
# 2. Return false if character not found
# 3. Check if last node is word end

# StartsWith:
# 1. Start at root, traverse prefix characters
# 2. Return false if character not found
# 3. Return true if all prefix chars found

class TrieNode:
   def __init__(self):
       self.children = {}  # Maps characters to child nodes
       self.isEndNode = False  # Marks end of word
       
class Trie:
   def __init__(self):
       self.root = TrieNode()

   def insert(self, word: str) -> None:
       currentNode = self.root
       
       for char in word:
           if char not in currentNode.children:
               currentNode.children[char] = TrieNode()
           currentNode = currentNode.children[char]
           
       currentNode.isEndNode = True

   def search(self, word: str) -> bool:
       currentNode = self.root
       
       for char in word:
           if char in currentNode.children:
               currentNode = currentNode.children[char]
           else:
               return False
               
       return currentNode.isEndNode

   def startsWith(self, prefix: str) -> bool:
       currentNode = self.root
       
       for char in prefix:
           if char in currentNode.children:
               currentNode = currentNode.children[char]
           else:
               return False
               
       return True
