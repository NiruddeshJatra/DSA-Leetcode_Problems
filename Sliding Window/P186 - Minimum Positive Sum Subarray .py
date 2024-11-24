# Time Complexity: O(n * (r - l + 1)), where n is the length of the `nums` array, and r - l + 1 represents the range of subarray lengths to check.  
# - Calculating the prefix sum array takes O(n).  
# - For each subarray length from `l` to `r`, we iterate over the array, resulting in a complexity of O(n * (r - l + 1)).  

# Space Complexity: O(n), as we store the prefix sum array, which has a size equal to the length of the `nums` array.  

# INTUITION:  
# The task is to find the minimum sum of all possible subarrays of lengths ranging from `l` to `r`.  
# To achieve this efficiently, we use a prefix sum array to calculate the sum of any subarray in O(1) time.  
# - The prefix sum at index `i` represents the sum of all elements from the start of the array up to index `i`.  
# - Using the prefix sum, the sum of a subarray from index `start` to `end` can be calculated as `prefixSum[end] - prefixSum[start]`.  
# - By iterating through all subarray lengths and all possible starting indices, we compare their sums and track the minimum.  

# ALGORITHM:  
# 1. Initialize `ans` to `float('inf')` to track the minimum subarray sum.  
# 2. Compute the prefix sum array for efficient subarray sum calculations.  
# 3. For each subarray length from `l` to `r`:  
#    - Use a sliding window approach to iterate through the array, calculating the subarray sum for each valid window.  
#    - Update `ans` with the minimum subarray sum encountered that is greater than zero.  
# 4. If no valid subarray sum is found, return -1; otherwise, return `ans`.

from typing import List

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        # Initialize the minimum sum to infinity
        minSum = float('inf')

        # Calculate prefix sum for efficient subarray sum calculation
        prefixSum = [0]
        for num in nums:
            prefixSum.append(prefixSum[-1] + num)

        # Iterate through all subarray lengths from l to r
        for length in range(l, r + 1):
            # Use a sliding window approach to check all subarrays of the current length
            for start in range(len(nums) - length + 1):
                end = start + length
                windowSum = prefixSum[end] - prefixSum[start]
                if windowSum > 0:
                    minSum = min(minSum, windowSum)

        # If no valid subarray is found, return -1; otherwise, return the minimum sum
        return minSum if minSum != float('inf') else -1


# Example Usage:
# solution = Solution()
# nums = [1, -2, 3, 4, -5, 6]
# l = 2
# r = 3
# print(solution.minimumSumSubarray(nums, l, r))  # Example Output: 1
