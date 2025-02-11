# Time Complexity:
# - O(N * W^2) where:
#   N = number of words in wordList
#   W = length of each word
# - For each word (N), we:
#   - Create W patterns of length W
#   - Each pattern creation takes O(W)
# - BFS traversal: O(N) words * O(W) patterns per word

# Space Complexity:
# - O(N * W) for adjacency list storing patterns
# - O(N) for queue and visited set
# - Overall space: O(N * W)

# INTUITION:
# Imagine playing word ladder game:
# "COLD" -> "CORD" -> "CARD" -> "WARD"
# Each step changes exactly one letter
#
# To find shortest transformation:
# 1. For each word, find all possible "patterns"
#    COLD -> *OLD, C*LD, CO*D, COL*
# 2. Group words by patterns they match
#    *OLD: COLD, HOLD, FOLD
#    C*LD: COLD, CALD
# 3. Use patterns to find connected words
# 4. BFS to find shortest path to target

# ALGORITHM:
# 1. Build pattern-based adjacency list:
#    - For each word, create all possible patterns
#    - Map each pattern to list of matching words
# 2. BFS from beginWord:
#    - For current word, find all its patterns
#    - Find unvisited words matching these patterns
#    - Add those words to queue
#    - Track transformation length
# 3. Return length when endWord found

class Solution:
   def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
       # Early exit if endWord not in wordList
       if endWord not in wordList:
           return 0
           
       # Add beginWord to wordList for pattern generation
       wordList.append(beginWord)
       
       # Build pattern-based adjacency list
       patternToWords = defaultdict(list)
       for word in wordList:
           # Generate all possible patterns for this word
           for i in range(len(word)):
               # Replace each character with * to create pattern
               pattern = word[:i] + "*" + word[i+1:]
               patternToWords[pattern].append(word)
       
       # BFS queue and visited set
       queue = deque([beginWord])
       visited = {beginWord}  # Using set for O(1) lookup
       transformationLength = 1
       
       # BFS traversal
       while queue:
           # Process all words at current level
           for _ in range(len(queue)):
               currentWord = queue.popleft()
               
               # Found target word
               if currentWord == endWord:
                   return transformationLength
                   
               # Try changing each character position
               for i in range(len(currentWord)):
                   # Generate pattern for current position
                   pattern = currentWord[:i] + "*" + currentWord[i+1:]
                   
                   # Check all words matching this pattern
                   for neighborWord in patternToWords[pattern]:
                       if neighborWord not in visited:
                           visited.add(neighborWord)
                           queue.append(neighborWord)
                           
           # Increment path length after processing each level
           transformationLength += 1
       
       # No transformation sequence found
       return 0
