# Time Complexity:
# - O(C) to build initial graph where C is total characters in all words
# - O(N*M) for comparing adjacent words where N is number of words and M is max word length
# - O(V + E) for topological sort where V is unique characters and E is character relationships
# - Overall: O(C + N*M + V + E)

# Space Complexity:
# - O(V + E) for adjacency list graph
# - O(V) for visited dictionary
# - O(V) for result array and recursion stack
# - Overall: O(V + E)

# INTUITION:
# This is alien dictionary problem where we need to find character ordering.
# By comparing adjacent words, we can build a graph where edge a->b means
# 'a' comes before 'b' in the dictionary. Then use topological sort to get order.
#
# Example:
# words = ["wrt", "wrf", "er", "ett", "rftt"]
#
# Compare adjacent words:
# "wrt" vs "wrf": t->f
# "wrf" vs "er": w->e
# "er" vs "ett": r->t
# "ett" vs "rftt": e->r
#
# Graph: 
# t->f
# w->e
# r->t
# e->r
#
# Topological sort gives: "wertf"

# ALGO:
# 1. Build character graph by comparing adjacent words:
#    - For first different chars a,b add edge a->b
#    - Handle invalid case: w1 longer than w2 but same prefix
# 2. Do topological sort using DFS:
#    - Track visited status to detect cycles
#    - Add chars to result in post-order
#    - Reverse result to get correct order
# 3. Return empty string if cycle detected
# 4. Otherwise return joined character order

class Solution:
   def foreignDictionary(self, words: List[str]) -> str:
       # Build graph of character relationships
       # Each char maps to set of chars that come after it
       graph = {c: set() for word in words for c in word}
       
       # Compare adjacent words to build edges
       for i in range(len(words) - 1):
           word1, word2 = words[i], words[i+1]
           minLength = min(len(word1), len(word2))
           
           # Invalid case: word1 longer but same prefix
           if len(word1) > len(word2) and word1[:minLength] == word2[:minLength]:
               return ""
               
           # Add edge for first different character
           for j in range(minLength):
               if word1[j] != word2[j]:
                   graph[word1[j]].add(word2[j])
                   break
                   
       # Topological sort using DFS
       visited = {}  # Track node status for cycle detection
       order = []    # Store character order
       
       def dfsTopSort(char: str) -> bool:
           # Return True if cycle detected
           if char in visited:
               return visited[char]
               
           visited[char] = True  # Mark as being visited
           
           # Visit neighbors
           for nextChar in graph[char]:
               if dfsTopSort(nextChar):
                   return True
                   
           # Add to result in post-order
           order.append(char)
           visited[char] = False  # Mark as done
           return False
           
       # Do topological sort from each unvisited char
       for char in graph:
           if dfsTopSort(char):
               return ""  # Cycle detected
               
       # Reverse to get correct order
       order.reverse()
       return "".join(order)
