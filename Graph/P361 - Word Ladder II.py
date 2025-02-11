# Time Complexity:
# - O(N * 26^L) where:
#   N = number of words in wordList
#   L = length of each word
#   26 is alphabet size for each position
# - Pattern generation: O(N * L)
# - BFS traversal: O(N * 26^L) in worst case
# - Backtracking: O(K) where K is number of valid paths

# Space Complexity:
# - O(N * L) for adjacency list
# - O(N) for queue, distance map
# - O(N * K) for predecessors list where K is branching factor
# - O(K * L) for result paths
# - Overall: O(N * L + N * K)

# INTUITION:
# Similar to word ladder, but need ALL shortest paths.
# Think of it like finding all possible routes between cities:
# hit -> hot -> dot -> dog -> cog
# hit -> hot -> lot -> log -> cog
#
# Key differences from regular word ladder:
# 1. Need to track ALL previous words that led to current
# 2. Can't mark words visited immediately (multiple paths)
# 3. Need backtracking to reconstruct all paths
#
# Like mapping a river delta:
# - Multiple streams can reach same point
# - Need to track all tributaries
# - Then trace back from end to start

# ALGORITHM:
# 1. Build pattern-based graph like regular word ladder
# 2. Modified BFS:
#    - Track distances to ensure shortest paths
#    - Store ALL predecessors at same level
#    - Process level by level to handle multiple paths
# 3. Backtracking to build paths:
#    - Start from endWord
#    - Recursively explore all predecessors
#    - Build paths in reverse

class Solution:
   def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
       # Early exit if endWord not in wordList
       if endWord not in wordList:
           return []
       
       # Create word set and add beginWord
       wordSet = set(wordList)
       wordSet.add(beginWord)
       
       # Build pattern-based adjacency list
       patternToWords = defaultdict(list)
       for word in wordSet:
           for i in range(len(word)):
               pattern = word[:i] + '*' + word[i+1:]
               patternToWords[pattern].append(word)
       
       # BFS initialization
       queue = deque([beginWord])
       levelDistance = {beginWord: 1}
       wordPredecessors = defaultdict(list)
       targetFound = False
       
       # Level by level BFS
       while queue and not targetFound:
           currentLevelSize = len(queue)
           currentLevelWords = set()
           
           # Process current level
           for _ in range(currentLevelSize):
               currentWord = queue.popleft()
               
               # Check if target reached
               if currentWord == endWord:
                   targetFound = True
               
               # Generate neighbors through patterns
               for i in range(len(currentWord)):
                   pattern = currentWord[:i] + '*' + currentWord[i+1:]
                   for neighborWord in patternToWords[pattern]:
                       # First time seeing this word
                       if neighborWord not in levelDistance:
                           levelDistance[neighborWord] = levelDistance[currentWord] + 1
                           wordPredecessors[neighborWord].append(currentWord)
                           currentLevelWords.add(neighborWord)
                       # Found another path of same length
                       elif levelDistance[neighborWord] == levelDistance[currentWord] + 1:
                           wordPredecessors[neighborWord].append(currentWord)
           
           # Add current level words to queue
           queue.extend(currentLevelWords)
           
           if targetFound:
               break
       
       # If endWord not reachable
       if not targetFound:
           return []
       
       # Backtrack to find all paths
       def backtrackPaths(currentWord, path):
           # Reached beginning of path
           if currentWord == beginWord:
               allPaths.append(path[::-1])  # Reverse to get correct order
               return
           
           # Try all predecessors
           for previousWord in wordPredecessors[currentWord]:
               backtrackPaths(previousWord, path + [previousWord])
       
       # Collect all paths
       allPaths = []
       backtrackPaths(endWord, [endWord])
       
       return allPaths
