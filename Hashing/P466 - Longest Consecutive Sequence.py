# Time Complexity:
# - O(n), where n is the number of elements in the input array
# - Although we have nested loops, each number is visited at most twice
# - The inner while loop only runs for sequence starting points

# Space Complexity:
# - O(n) to store all numbers in a set for O(1) lookup operations

# INTUITION:
# The problem asks for the length of the longest consecutive sequence
# Key insight: Only start counting from the beginning of each sequence
# Strategy:
# - Use a set for O(1) lookups
# - For each number, check if it's the start of a sequence (no predecessor)
# - If it's a sequence start, count consecutive numbers until the sequence breaks
# Example:
# nums = [100,4,200,1,3,2]
# Sequences: [1,2,3,4] (length 4), [100] (length 1), [200] (length 1)
# We only start counting from 1, 100, and 200 (numbers without predecessors)

# ALGO:
# 1. Convert array to set for fast lookups
# 2. For each number in the set:
#    - Check if it's the start of a sequence (num-1 not in set)
#    - If it's a sequence start, count consecutive numbers
#    - Track the maximum sequence length found
# 3. Return the maximum consecutive sequence length

class Solution:
   def longestConsecutive(self, nums: List[int]) -> int:
       # Convert to set for O(1) lookup operations
       numSet = set(nums)
       maxSequenceLength = 0
       
       # Check each number in the set
       for currentNum in numSet:
           currentSequenceLength = 0
           
           # Only start counting if this is the beginning of a sequence
           # (i.e., currentNum - 1 is not in the set)
           if currentNum - 1 not in numSet:
               sequenceNum = currentNum
               
               # Count consecutive numbers in the sequence
               while sequenceNum in numSet:
                   currentSequenceLength += 1
                   sequenceNum += 1
           
           # Update maximum sequence length found so far
           maxSequenceLength = max(maxSequenceLength, currentSequenceLength)
       
       return maxSequenceLength
