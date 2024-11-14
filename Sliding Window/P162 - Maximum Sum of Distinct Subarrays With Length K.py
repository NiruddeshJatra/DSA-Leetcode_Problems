# Time Complexity: O(n), where n is the length of nums.
# We use a sliding window approach, moving i and j through the array once in total.

# Space Complexity: O(k), where k is the window size.
# We use a set to store up to k unique elements in the current window.

# INTUITION:
# This problem requires finding the maximum sum of a subarray with unique elements of fixed length k. 
# Using a sliding window approach allows us to maintain the fixed size constraint while adjusting the 
# window to ensure all elements are unique. By expanding `j` to include elements in the window and contracting `i` 
# when duplicates arise, we maintain the unique property in the window of length k. This approach is efficient, 
# avoiding redundant calculations and reducing complexity compared to re-evaluating all possible subarrays.

# ALGO:
# 1. Initialize `i` and `j` pointers, with `i` marking the start and `j` expanding the window end.
# 2. Maintain a set `visited` for unique elements in the current window and `windowSum` for the sum of elements.
# 3. Expand window by adding `nums[j]`:
#    - If `nums[j]` is in `visited`, shrink from `i` until `nums[j]` is removed, ensuring uniqueness.
#    - Add `nums[j]` to `visited` and `windowSum`.
# 4. If the window length (j - i + 1) reaches k, calculate and update the maximum sum, then slide `i` right.
# 5. Continue until `j` reaches the end of the array.
# 6. Return the maximum subarray sum found.

from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans, windowSum = 0, 0
        visited = set()
        i = j = 0
        
        while j < len(nums):
            while nums[j] in visited:
                windowSum -= nums[i]
                visited.remove(nums[i])
                i += 1
            
            windowSum += nums[j]
            visited.add(nums[j])
            
            if (j - i + 1) == k:
                ans = max(ans, windowSum)
                windowSum -= nums[i]
                visited.remove(nums[i])
                i += 1
            
            j += 1

        return ans
