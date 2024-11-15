# Time Complexity: O(n), where n is the length of `arr`.
# We iterate through the array once, maintaining the sum of elements in a sliding window.

# Space Complexity: O(1).
# The algorithm uses a fixed number of variables (`ans`, `windowSum`, `start`), making it space-efficient.

# INTUITION:
# This problem requires finding the count of subarrays of fixed length `k` with an average greater than or equal to `threshold`.  
# By using a sliding window approach, we can efficiently calculate the sum of elements in each subarray of size `k` without repeatedly summing over all elements.  
# The sliding window adjusts by adding the next element in the array to the window and removing the first element of the previous window, allowing the sum to be updated in constant time.  
# Checking the average of the current window against the `threshold` ensures we count only the valid subarrays.  
# This approach avoids the inefficiency of recalculating sums for overlapping subarrays, making it optimal for this problem.

# ALGO:
# 1. Initialize `ans` to count valid subarrays, `windowSum` for the current subarray sum, and `start` to track the start of the sliding window.
# 2. Traverse the array:
#    - Add the current element to `windowSum`.
#    - If the window size reaches `k`:
#        - Check if the average (`windowSum / k`) is greater than or equal to `threshold`. If yes, increment `ans`.
#        - Remove the element at `start` from `windowSum` to slide the window forward.
#        - Increment `start`.
# 3. Return `ans`, the total count of valid subarrays.

from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        validSubarrayCount = 0  # Renamed `ans` for clarity
        windowSum = 0
        start = 0

        for i in range(len(arr)):
            windowSum += arr[i]

            if (i - start + 1) == k:  # When window size reaches `k`
                if windowSum / k >= threshold:
                    validSubarrayCount += 1
                windowSum -= arr[start]  # Slide the window
                start += 1

        return validSubarrayCount
