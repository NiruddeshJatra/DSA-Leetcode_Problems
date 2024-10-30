# Problem: Given an integer array `nums`, return an array `ans` where `ans[i]` is the product of all the elements in `nums` except `nums[i]`.

# Time Complexity: O(n), where n is the number of elements in `nums`.
# This is because we make two passes through the list to calculate the products from the left and right.

# Space Complexity: O(1), since `ans` is used for the output without extra space.

# ALGO:
# 1. Initialize `ans` with ones, which will store the products.
# 2. Compute the product of all elements to the left of each index:
#    - Set `cur` to 1, representing the cumulative product.
#    - Traverse `nums` from left to right.
#    - For each element, update `ans[i]` with `cur`, then multiply `cur` by `nums[i]`.
# 3. Compute the product of all elements to the right of each index:
#    - Reset `cur` to 1.
#    - Traverse `nums` from right to left.
#    - For each element, update `ans[i]` with `cur`, then multiply `cur` by `nums[i]`.
# 4. Return `ans` as the final result.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Step 1: Initialize `ans` with 1s
        ans = [1] * len(nums)

        # Step 2: Calculate products of elements to the left of each index
        cur = 1
        for i in range(len(nums)):
            ans[i] *= cur
            cur *= nums[i]

        # Step 3: Calculate products of elements to the right of each index
        cur = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= cur
            cur *= nums[i]

        # Step 4: Return the result array
        return ans

# Example usage
# nums = [1, 2, 3, 4]
# sol = Solution()
# print(sol.productExceptSelf(nums))  # Expected output: [24, 12, 8, 6]
