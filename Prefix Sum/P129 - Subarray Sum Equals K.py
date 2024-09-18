# Time Complexity: O(n), where n is the length of the input list `nums`. 
# This is because we iterate through the list once and perform constant time operations like checking and updating the hash map.
# Space Complexity: O(n), as we store the prefix sums in a dictionary. In the worst case, all prefix sums are unique, leading to n entries in the dictionary.

# INTUITION:
# The idea is to use a hash map (`prefixSum`) to store the cumulative sums (prefix sums) and their frequencies as we iterate through the array. 
# For each element, we compute the cumulative sum up to that point and check how many subarrays end at that element and sum to `k`. 
# By looking at the difference between the current cumulative sum and `k`, we can determine if there exists a subarray that sums to `k`.

# ALGO:
# 1. Initialize a variable `sum` to keep track of the cumulative sum and a dictionary `prefixSum` to store the frequency of each cumulative sum.
# 2. Set `prefixSum[0] = 1` to handle the case where a subarray starting from index 0 sums to `k`.
# 3. Iterate through each number in `nums`:
#    3.1. Update the cumulative sum.
#    3.2. Check if `sum - k` exists in the dictionary `prefixSum`. If it does, it means there is a subarray that sums to `k`.
#    3.3. Increment the count of such subarrays by the frequency of `sum - k` in `prefixSum`.
#    3.4. Update the frequency of the current cumulative sum in `prefixSum`.
# 4. Return the total count of subarrays that sum to `k`.

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Step 1: Initialize variables
        cnt, sum = 0, 0  # cnt will store the count of subarrays, sum will store the cumulative sum
        prefixSum = {0: 1}  # Initialize the prefixSum dictionary with {0:1} to handle edge cases
        
        # Step 2: Iterate through the nums array
        for num in nums:
            # Step 2.1: Update the cumulative sum
            sum += num
            
            # Step 2.2: Check if sum - k exists in the prefixSum dictionary
            cnt += prefixSum.get(sum - k, 0)
            
            # Step 2.3: Update the frequency of the current sum in prefixSum
            prefixSum[sum] = prefixSum.get(sum, 0) + 1
        
        # Step 3: Return the count of subarrays that sum to k
        return cnt
