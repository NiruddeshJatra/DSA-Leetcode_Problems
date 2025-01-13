# Time Complexity:
# - O(N log N) due to the initial sorting of the array
# - The subsequent loop takes O(N), but is dominated by the sorting complexity

# Space Complexity:
# - O(1) as we only use a constant amount of extra space regardless of input size

# INTUITION:
# The problem involves finding the minimum possible difference between max and min elements after applying
# +K or -K to each element. The key insight is that after sorting:
# 1. For any optimal solution, there will be a point where elements before it are increased by K
#    and elements after it are decreased by K
# 2. We can iterate through each possible "splitting point" to find the minimum range
# 3. For each split, we need to consider four values: nums[0]+K, nums[i]+K, nums[i+1]-K, nums[-1]-K

# ALGORITHM:
# 1. Sort the array to make elements sequential
# 2. Calculate initial range (max - min) as baseline result
# 3. For each possible splitting point i:
#    - Left side elements (0 to i) will be increased by K
#    - Right side elements (i+1 to end) will be decreased by K
#    - Calculate new max as max(last_element - K, current_element + K)
#    - Calculate new min as min(first_element + K, next_element - K)
#    - Update result if new range is smaller
# 4. Return the minimum range found

class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        # Edge case: empty array or single element
        if len(nums) <= 1:
            return 0
        
        # Sort the array to make elements sequential
        nums.sort()
        
        # Initialize the result with the current range
        currentMax = nums[-1]
        currentMin = nums[0]
        minRange = currentMax - currentMin
        
        # Try each possible splitting point
        for i in range(len(nums) - 1):
            # For elements up to index i: add K
            # For elements after index i: subtract K
            potentialMax = max(currentMax - k, nums[i] + k)
            potentialMin = min(currentMin + k, nums[i + 1] - k)
            
            # Update minimum range if current solution is better
            minRange = min(minRange, potentialMax - potentialMin)
        
        return minRange
