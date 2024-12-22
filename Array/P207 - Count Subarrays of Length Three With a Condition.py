# Time Complexity: O(n), where n is the length of the array.
# - The loop iterates through the array once to check conditions for each triplet.

# Space Complexity: O(1).
# - No additional space is used apart from variables.

# ALGORITHM:
# 1. Initialize a variable `count` to 0 to store the count of valid subarrays.
# 2. Iterate through the array using an index `i` from 0 to `len(nums) - 3`:
#    - Check if the triplet formed by `nums[i]`, `nums[i+1]`, and `nums[i+2]` satisfies the condition:
#      `(nums[i] + nums[i+2]) * 2 == nums[i+1]`.
#    - If the condition is satisfied, increment `count` by 1.
# 3. Return the value of `count`.

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0  # Initialize the count of valid subarrays.
        
        # Iterate through the array to check triplets.
        for i in range(len(nums) - 2):
            # Check if the middle element is twice the average of the outer two elements.
            if (nums[i] + nums[i+2]) * 2 == nums[i+1]:
                count += 1

        return count

# Example Usage:
# Input: nums = [1, 2, 1, 4, 3]
# Output: 2
# Explanation: The valid subarrays are [1, 2, 1] and [2, 1, 4].
solution = Solution()
print(solution.countSubarrays([1, 2, 1, 4, 3]))  # Output: 2
