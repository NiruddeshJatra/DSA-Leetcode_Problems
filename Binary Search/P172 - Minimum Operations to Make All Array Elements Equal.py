# Time Complexity: O((m + n) * log(n)), where `n` is the length of `nums` and `m` is the length of `queries`.  
# - Sorting `nums` takes O(n * log(n)).  
# - For each query, we perform a binary search (O(log(n))) and calculate increments and decrements in O(1).  
# - Total complexity for processing `m` queries is O(m * log(n)).

# Space Complexity: O(n), where `n` is the length of `nums`.  
# - The prefix sum array stores cumulative sums, requiring O(n) space.

# INTUITION:  
# The task is to determine the minimum operations needed to make all elements in `nums` equal to the value of each `query`.  
# Using a sorted `nums` and a prefix sum array, we can efficiently compute the total increment and decrement operations required for each query.  
# The idea is to split the problem into two parts:  
# 1. **Increment operations**: For elements smaller than the query value.  
# 2. **Decrement operations**: For elements larger than the query value.  
# By finding the index of the first element greater than or equal to `query` using binary search,  
# we can divide the array into two regions to calculate the increments and decrements in O(1).

# ALGO:  
# 1. Sort the array `nums` in ascending order.  
# 2. Create a prefix sum array for `nums` to store cumulative sums for efficient range sum queries.  
# 3. For each `query`:  
#    - Use binary search to find the index `i` of the first element >= `query`.  
#    - Calculate the total increment operations for the left part (elements < `query`).  
#    - Calculate the total decrement operations for the right part (elements >= `query`).  
#    - Append the sum of increment and decrement operations to `ans`.  
# 4. Return the final `ans` array.

from typing import List
from bisect import bisect_left

class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        ans = []
        nums.sort()
        prefixSum = [0]
        total, n = 0, len(nums)

        # Build prefix sum array
        for num in nums:
            total += num
            prefixSum.append(total)

        # Process each query
        for query in queries:
            i = bisect_left(nums, query)  # Binary search for the first element >= query
            increment = query * i - prefixSum[i]  # Cost to increment elements < query
            decrement = prefixSum[n] - prefixSum[i] - query * (n - i)  # Cost to decrement elements >= query
            ans.append(increment + decrement)

        return ans
