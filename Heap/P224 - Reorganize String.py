# Time Complexity:
# - O(N log K) where N is length of string and K is number of unique characters
#   - Building frequency map: O(N)
#   - Creating heap of K elements: O(K log K)
#   - N heap operations: O(N log K)
#   - Building final string: O(N)

# Space Complexity:
# - O(K) where K is number of unique characters
#   - Counter map stores K entries
#   - Heap stores K elements
#   - Answer array builds up to N but reuses space

# INTUITION:
# To reorganize string with no adjacent same characters:
# - Most frequent characters must be spaced out
# - Use max heap to always get most frequent remaining char
# - Keep track of previously used char to avoid adjacency
# - If can't use most frequent (would be adjacent), use next
# This is greedy approach using heap to always pick valid max frequency char

# ALGO:
# 1. Create frequency map using Counter
# 2. Build max heap with (-frequency, char) pairs
# 3. While heap not empty:
#    - Pop most frequent char
#    - Add to result
#    - If previous char has remaining count:
#      * Push it back to heap
#    - Update previous char info
# 4. Return result if valid length, empty if impossible

class Solution:
   def reorganizeString(self, s: str) -> str:
       # Build frequency map
       freq = Counter(s)
       
       # Create max heap with frequencies
       heap = []
       for char, count in freq.items():
           heapq.heappush(heap, (-count, char))
       
       # Build result string
       ans = []
       prevCount, prevChar = 0, ''
       
       while heap:
           # Get most frequent char
           count, char = heapq.heappop(heap)
           ans.append(char)
           
           # Add previous char back to heap if has remaining count
           if prevCount < 0:
               heapq.heappush(heap, (prevCount, prevChar))
           
           # Update previous char info
           count += 1
           prevCount, prevChar = count, char
       
       # Return result if valid, empty if impossible
       return ''.join(ans) if len(ans) == len(s) else ''
