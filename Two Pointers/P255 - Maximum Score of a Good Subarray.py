# Time Complexity: 
# - O(N), where N is the length of nums array
# - Each element is considered at most once
# - Two pointers (i,j) traverse array in single pass

# Space Complexity:
# - O(1), only uses a constant amount of extra space
# - Just variables for pointers, running min, and result

# INTUITION:
# For each subarray containing index k, score = min(subarray) * length.
# Using two pointers expanding from k is ideal because:
# 1. Valid subarrays must contain index k
# 2. Can greedily expand towards larger elements
# 3. Minimum value can only decrease as we expand
# 4. Length increases by 1 with each expansion
# 5. Can efficiently track running minimum

# ALGO:
# 1. Start both pointers at index k
# 2. While can expand either left or right:
#    - Choose direction with larger next element
#    - Update running minimum with new element
#    - Calculate score = current_min * length
#    - Update max score if larger
# 3. Return maximum score found

class Solution:
   def maximumScore(self, nums: List[int], k: int) -> int:
       # Initialize pointers at index k
       leftPtr = rightPtr = k
       maxScore = currentMin = nums[k]
       
       # Expand window while possible
       while leftPtr > 0 or rightPtr < len(nums) - 1:
           # Get next values (0 if out of bounds)
           leftValue = nums[leftPtr - 1] if leftPtr else 0
           rightValue = nums[rightPtr + 1] if rightPtr < len(nums) - 1 else 0
           
           # Expand towards larger value
           if leftValue < rightValue:
               rightPtr += 1
               currentMin = min(currentMin, nums[rightPtr])
           else:
               leftPtr -= 1
               currentMin = min(currentMin, nums[leftPtr])
           
           # Update maximum score
           windowLength = rightPtr - leftPtr + 1
           currentScore = currentMin * windowLength
           maxScore = max(maxScore, currentScore)
       
       return maxScore
