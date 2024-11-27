# Time Complexity: O(n + m), where n is the length of `nums1` and m is the length of `nums2`.
# - Creating the Counter for `nums2` takes O(m).
# - Iterating through `nums1` to check and reduce counts takes O(n).

# Space Complexity: O(m), where m is the size of `nums2`.
# - The space is used to store the frequency count of elements in `nums2`.

# INTUITION:
# - We need to find the intersection of two arrays such that each element in the result appears as many times as it shows in both arrays.
# - Using a frequency count of one array allows us to efficiently determine how many times a value can be added to the result while iterating through the other array.

# ALGORITHM:
# 1. Count the frequency of each element in `nums2` using a `Counter`.
# 2. Iterate through `nums1`:
#    - If the current element exists in the `Counter`, add it to the result and decrease its frequency in the `Counter`.
#    - If the frequency of the element in the `Counter` becomes zero, remove it from the `Counter` to save space.
# 3. Return the resulting list.

from collections import Counter
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Count the occurrences of elements in nums2
        nums2Count = Counter(nums2)
        result = []
        
        # Iterate through nums1 and find intersections
        for num in nums1:
            if num in nums2Count:
                result.append(num)  # Add to the result
                nums2Count[num] -= 1  # Decrement the count
                if nums2Count[num] == 0:
                    del nums2Count[num]  # Remove element if count reaches 0

        return result

# Example Usage:
# Input:
# nums1 = [1, 2, 2, 1]
# nums2 = [2, 2]
# Output: [2, 2]
# Explanation: The elements 2 appear twice in both arrays.
# 
# Input:
# nums1 = [4, 9, 5]
# nums2 = [9, 4, 9, 8, 4]
# Output: [4, 9]
# Explanation: The elements 4 and 9 appear in both arrays (order doesn't matter).
