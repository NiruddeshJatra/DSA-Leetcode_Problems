# Time Complexity: O(n), where n is the number of elements in `nums`.
# We traverse the list once to identify the majority element, making this a linear time solution.

# Space Complexity: O(1), as we only use a constant amount of extra space for variables `ans` and `n`.

# INTUITION:
# The majority element in an array is the element that appears more than ⌊n/2⌋ times.
# Using the Boyer-Moore Voting Algorithm, we can identify this element by maintaining a candidate (`ans`) and a count (`n`).
# If `n` becomes zero, we update `ans` to the current element, assuming it could potentially be the majority.

# ALGO:
# 1. Initialize the first element as the candidate (`ans`) and set the count (`n`) to 1.
# 2. Traverse through the list starting from the second element:
#    - If the current element matches `ans`, increase `n` by 1.
#    - If it doesn’t match, decrease `n` by 1.
#    - If `n` becomes zero, update `ans` to the current element and reset `n` to 1.
# 3. Return `ans` as the majority element.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Step 1: Initialize the candidate (`ans`) and count (`n`)
        ans = nums[0]
        n = 1

        # Step 2: Traverse the array and apply Boyer-Moore Voting logic
        for i in nums[1:]:
            if ans == i:
                n += 1
            else:
                n -= 1
            if n < 0:
                ans = i
                n = 1

        # Step 3: Return the majority element
        return ans

# Example usage
# nums = [3, 2, 3]
# sol = Solution()
# print(sol.majorityElement(nums))  # Expected output: 3
