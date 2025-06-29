# Time Complexity:
# - O(N * M), where N is the number of words and M is the average length of words.
# - We compute LCP for adjacent pairs (O(N * M)), build prefix arrays (O(N)), and for each word check candidates (O(M) for direct LCP computation).

# Space Complexity:
# - O(N), for storing the adjacentLcp array and prefix maximum arrays.

# INTUITION:
# For each word at position i, we want to find the longest common prefix it can have with any other word in the array.
# The key insight is that we only need to consider:
# 1. Maximum LCP from all pairs to the left of position i
# 2. Maximum LCP from all pairs to the right of position i  
# 3. Direct LCP between word[i-1] and word[i+1] (skipping current word)
# 
# We precompute LCP for all adjacent pairs, then use prefix maximum arrays to efficiently find the maximum
# LCP values in left and right segments. This avoids checking all possible pairs for each word.

# ALGO:
# 1. Handle edge case: if array has ≤1 words, return [0]
# 2. Compute LCP for all adjacent word pairs and store in adjacentLcp array
# 3. Build prefixMaxLeft: for each position, store max LCP from all pairs to the left
# 4. Build prefixMaxRight: for each position, store max LCP from all pairs to the right  
# 5. For each word position i, collect candidate LCP values:
#    - Max LCP from left segment (if exists)
#    - Max LCP from right segment (if exists)
#    - Direct LCP between words[i-1] and words[i+1] (if both exist)
# 6. Take maximum of all candidates for each position

from typing import List

class Solution:
   def longestCommonPrefix(self, words: List[str]) -> List[int]:
       def computeLcp(word1, word2):
           commonLength = 0
           for i in range(min(len(word1), len(word2))):
               if word1[i] != word2[i]:
                   break
               commonLength += 1
           return commonLength

       numWords = len(words)
       if numWords <= 1:
           return [0]
       
       # Compute LCP for all adjacent pairs
       adjacentLcp = []
       for i in range(numWords - 1):
           adjacentLcp.append(computeLcp(words[i], words[i + 1]))

       # Build prefix maximum arrays
       prefixMaxLeft = [0] * (numWords - 1)
       prefixMaxRight = [0] * (numWords - 1)

       # Fill prefix maximum from left
       prefixMaxLeft[0] = adjacentLcp[0]
       for i in range(1, numWords - 1):
           prefixMaxLeft[i] = max(prefixMaxLeft[i - 1], adjacentLcp[i])

       # Fill prefix maximum from right
       prefixMaxRight[-1] = adjacentLcp[-1]
       for i in range(numWords - 3, -1, -1):
           prefixMaxRight[i] = max(prefixMaxRight[i + 1], adjacentLcp[i])
           
       result = []
       for i in range(numWords):
           candidates = []

           # Max LCP from left segment
           if i >= 2:
               candidates.append(prefixMaxLeft[i - 2])

           # Max LCP from right segment
           if i < numWords - 2:
               candidates.append(prefixMaxRight[i + 1])
               
           # Direct LCP between neighbors (skipping current word)
           if 0 < i < numWords - 1:
               candidates.append(computeLcp(words[i - 1], words[i + 1]))

           result.append(max(candidates) if candidates else 0)

       return result
