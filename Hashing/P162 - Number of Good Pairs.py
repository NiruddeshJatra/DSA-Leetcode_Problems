# Problem: Count the number of "good" pairs in an array `nums`, where a pair `(i, j)` is "good" if `nums[i] == nums[j]` and `i < j`.

# Time Complexity: O(n), where n is the number of elements in `nums`.
# This is because we make a single pass through the list to count occurrences and calculate "good" pairs.

# Space Complexity: O(n), as we use a hash map to store counts of elements in `nums`.

# ALGO:
# 1. Initialize `ans` to store the count of good pairs and an empty dictionary `hashmap` to track occurrences of each number.
# 2. For each element `i` in `nums`:
#    - If `i` exists in `hashmap`, increment `ans` by the count of `i` (this count represents the number of previous identical values).
#    - Increment the count of `i` in `hashmap`.
# 3. Return `ans`, which contains the total count of good pairs.

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # Step 1: Initialize answer and hashmap for counting occurrences
        ans = 0
        hashmap = {}

        # Step 2: Traverse through each element in `nums`
        for i in nums:
            # If `i` is already in hashmap, increment `ans` by its count
            if i in hashmap:
                ans += hashmap[i]
                hashmap[i] += 1
            else:
                # Otherwise, add `i` to hashmap with count 1
                hashmap[i] = 1

        # Step 3: Return the total number of good pairs
        return ans

# Example usage
# nums = [1, 2, 3, 1, 1, 3]
# sol = Solution()
# print(sol.numIdenticalPairs(nums))  # Expected output: 4
