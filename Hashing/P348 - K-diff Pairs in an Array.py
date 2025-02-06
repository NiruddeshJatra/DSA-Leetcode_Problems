# Time Complexity:
# - O(N) where N is the length of input array
# - Building frequency counter takes O(N)
# - Iterating through unique numbers takes O(N) worst case 
# - Hash table lookups are O(1)

# Space Complexity:
# - O(N) for the frequency counter hashtable
# - In worst case all numbers are unique
# - Only one variable needed for result counter

# INTUITION:
# For each unique number x, we need to find if x+k exists:
# - If k=0: Look for numbers that appear more than once
# - If k>0: Look for pairs (x, x+k)
# Using a frequency counter lets us:
# - Find duplicates easily for k=0 case
# - Do O(1) lookups to find pairs
# Example: nums=[3,1,4,1,5], k=2
# freq={1:2, 3:1, 4:1, 5:1}
# Found pairs: (1,3), (3,5)

# ALGO:
# 1. Create frequency counter for all numbers
# 2. For each unique number x:
#    - If k=0: Check if x appears more than once
#    - If k>0: Check if x+k exists in counter
# 3. Return total pairs found

class Solution:
   def findPairs(self, nums: List[int], k: int) -> int:
       # Build frequency counter
       numFrequency = Counter(nums)
       pairCount = 0
       
       # Check each unique number
       for num in numFrequency:
           if k == 0:
               # For k=0, need numbers appearing more than once
               if numFrequency[num] > 1:
                   pairCount += 1
           else:
               # For k>0, look for num+k
               if num + k in numFrequency:
                   pairCount += 1
       
       return pairCount
