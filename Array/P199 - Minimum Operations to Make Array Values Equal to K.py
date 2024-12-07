# Time Complexity: O(n), where n is the length of the input array `nums`.  
# - Creating a set from the input array takes O(n).  
# - Finding the minimum element in the set takes O(n).  
# - Iterating through the set to count numbers greater than `k` takes O(n).  
# Thus, the overall time complexity is O(n).

# Space Complexity: O(u), where `u` is the number of unique elements in the input array.  
# - Converting the input list to a set requires space proportional to the number of unique elements.  
# No additional significant space is used, so the space complexity is O(u).

# INTUITION:  
# The task is to find the minimum number of operations required to make all elements in `nums` equal to `k`.  
# Each operation allows you to reduce all elements greater than a valid threshold `h` to `h`.  
# The key observations are:  
# 1. If the minimum value in the array is less than `k`, it is impossible to make all elements equal to `k`, as you cannot increase elements.  
# 2. For all elements greater than `k`, each unique value needs to be reduced step-by-step, resulting in one operation per unique value above `k`.  
# This leads to a straightforward solution: count all unique elements greater than `k`.

# ALGO:  
# 1. Convert the input list `nums` into a set to remove duplicates, as only unique values matter for the operations.  
# 2. Check if the minimum value in the set is less than `k`. If so, return `-1`.  
# 3. Iterate through the set and count how many unique values are greater than `k`.  
# 4. Return the count as the result.

from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Step 1: Remove duplicates by converting to a set
        nums = set(nums)

        # Step 2: Check if it is impossible to make all elements equal to `k`
        if min(nums) < k:
            return -1

        # Step 3: Count unique numbers greater than `k`
        operations = 0
        for num in nums:
            if num > k:
                operations += 1

        # Step 4: Return the total operations needed
        return operations
