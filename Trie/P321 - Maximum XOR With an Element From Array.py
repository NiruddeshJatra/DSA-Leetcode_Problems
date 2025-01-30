# Time Complexity:
# - O(N*32 + Q*32) where N is length of nums array and Q is number of queries
# - Insert: O(32) = O(1) for each number as we process 32 bits
# - FindMax: O(32) = O(1) for each query as we traverse 32 bits
# - Overall complexity dominated by sorting: O(NlogN + QlogQ)

# Space Complexity:
# - O(N*32) for the Trie structure in worst case
# - Each number can potentially create 32 new nodes
# - Additional O(Q) space for storing results

# INTUITION:
# To maximize XOR of two numbers, we want opposite bits at each position whenever possible
# Using a Trie data structure where each level represents a bit (from MSB to LSB):
# - We can efficiently find a number with maximum XOR by traversing opposite bits
# - Sort numbers and queries by limit to handle constraints efficiently
# Example: For num = 4 (100) and candidates [2(010), 7(111)]
# We want opposite bits when possible: 7 gives better XOR than 2

# ALGO:
# 1. Build Trie class to store numbers in binary form:
#    - Each node represents a bit (0 or 1)
#    - Insert numbers by breaking into bits
# 2. For each number:
#    - Convert to binary
#    - Store each bit in Trie
# 3. For finding max XOR:
#    - Try to go opposite bit when possible
#    - If not possible, take available bit
# 4. Process queries:
#    - Sort by limit to process numbers efficiently
#    - Insert valid numbers into Trie
#    - Find maximum XOR for each query

class Trie:
   def __init__(self):
       self.root = {}  # Dictionary to store binary representation
       
   def insert(self, number: int) -> None:
       currentNode = self.root
       # Process from MSB (31) to LSB (0)
       for bitPosition in range(31, -1, -1):
           currentBit = 1 if number & (1 << bitPosition) else 0
           if currentBit not in currentNode:
               currentNode[currentBit] = {}
           currentNode = currentNode[currentBit]
           
   def findMax(self, targetNum: int) -> int:
       if not self.root:  # Empty Trie
           return -1
           
       currentNode = self.root
       maxXor = 0
       
       # Try to choose opposite bits when possible
       for bitPosition in range(31, -1, -1):
           targetBit = 0 if targetNum & (1 << bitPosition) else 1
           
           if targetBit in currentNode:
               currentNode = currentNode[targetBit]
               maxXor |= (1 << bitPosition)
           else:
               currentNode = currentNode[1 - targetBit]
               
       return maxXor

class Solution:
   def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
       nums.sort()  # Sort for processing queries by limit
       
       # Sort queries by limit (m) while keeping original indices
       queriesWithIndices = sorted(enumerate(queries), key=lambda x: x[1][1])
       
       trie = Trie()
       results = [-1] * len(queries)
       currentNumIndex = 0
       
       # Process each query
       for originalIndex, (targetNum, limit) in queriesWithIndices:
           # Insert all numbers <= limit into trie
           while currentNumIndex < len(nums) and nums[currentNumIndex] <= limit:
               trie.insert(nums[currentNumIndex])
               currentNumIndex += 1
               
           results[originalIndex] = trie.findMax(targetNum)
           
       return results
