# Time Complexity:
# - O(N) to create frequency counter
# - O(N) to iterate through unique frequencies
# - Overall O(N)

# Space Complexity:
# - O(N) for frequency counter
# - O(1) additional space
# - Overall O(N)

# INTUITION:
# Longest Harmonious Subsequence:
# 1. Must contain two different numbers
# 2. Difference between numbers is exactly 1
# 3. Use frequency counter to track occurrences
# Example: [1,3,2,2,5,2,3,7]
# Valid subsequences:
# - 3,2,2,2 (length 4)
# - 3,2 (length 2)
# - 2,1 (length 2)

# ALGO:
# 1. Create frequency counter
# 2. For each unique number x:
#    - Check if x+1 exists in frequency counter
#    - If exists, calculate total length
#    - Update max harmonious subsequence
# 3. Return maximum length found

def findLHS(self, nums: List[int]) -> int:
   # Count frequency of each number
   numFrequencies = Counter(nums)
   maxHarmoniousLength = 0
   
   # Check each unique number
   for num in numFrequencies:
       # Check if x+1 exists
       if num + 1 in numFrequencies:
           # Calculate total length
           currentLength = numFrequencies[num] + numFrequencies[num + 1]
           maxHarmoniousLength = max(maxHarmoniousLength, currentLength)
   
   return maxHarmoniousLength
