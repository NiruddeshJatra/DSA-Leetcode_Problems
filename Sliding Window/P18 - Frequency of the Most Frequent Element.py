# Time Complexity: O(n log n), where n is the length of the input array `nums`.
# The sorting operation takes O(n log n), and the sliding window traversal of the array takes O(n).

# Space Complexity: O(1).
# No additional space is used apart from a few variables.

# INTUITION:
# This problem revolves around maximizing the frequency of a single number in the array using at most `k` increments. 
# By sorting the array, we focus on making consecutive smaller elements equal to the largest element in the current window.
# The key idea is to calculate the `totalDifference` between the largest element in the window and all other elements in the window. 
# If this `totalDifference` exceeds `k`, the window needs to shrink from the right. This ensures that the operations are within the allowed limit, making the solution optimal.

# ALGO:
# 1. Sort the array `nums` to simplify managing consecutive elements.
# 2. Initialize variables:
#    - `ans` to store the maximum frequency found.
#    - `totalDifference` to track the sum of differences in the current window.
#    - `i` to mark the right boundary of the current window.
# 3. Traverse the array in reverse using `j` as the left boundary of the current window:
#    - Add the difference between the largest element (`nums[i]`) and the current element (`nums[j]`) to `totalDifference`.
#    - If `totalDifference` exceeds `k`, shrink the window by adjusting `i` and reducing `totalDifference`.
# 4. Update the count of elements in the window (`cnt`) and calculate the maximum frequency (`ans`).
# 5. Return `ans` after processing all elements.

from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        maxFrequency, windowCount = 1, 1
        totalDifference = 0
        right = len(nums) - 1
        for left in range(len(nums) - 2, -1, -1):
            totalDifference += nums[right] - nums[left]

            if right > 0 and totalDifference > k:
                totalDifference -= (nums[right] - nums[right - 1]) * windowCount
                right -= 1
                windowCount -= 1

            windowCount += 1
            maxFrequency = max(maxFrequency, windowCount)

        return maxFrequency
