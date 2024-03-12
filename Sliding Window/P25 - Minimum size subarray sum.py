class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        # INTUITION:
        # We use a sliding window approach to find the minimum length subarray
        # whose sum is greater than or equal to the target.

        # ALGO:
        # 1. Initialize variables 'ans' and 'total'. 'ans' will hold the minimum length of subarray found so far, and 'total' will hold the current sum of the subarray.
        # 2. Initialize pointers 'l' and 'r' to 0.
        # 3. Loop through the array until 'r' reaches the end:
        #     3.1 Add the element at 'r' to 'total'.
        #     3.2 While 'total' is greater than or equal to 'target':
        #         3.2.1 Update 'ans' with the minimum length found so far.
        #         3.2.2 Subtract the element at 'l' from 'total' and move 'l' to the right.
        #     3.3 Move 'r' to the right.
        # 4. If 'ans' remains unchanged (indicating no subarray was found), return 0. Otherwise, return 'ans'.

        ans, total = 10**18, 0  # Initialize 'ans' to a large value and 'total' to 0
        l, r = 0, 0  # Initialize pointers 'l' and 'r'

        while r < len(nums):  # Loop until 'r' reaches the end of the array
            total += nums[r]  # Add the element at 'r' to 'total'

            while total >= target:  # While 'total' is greater than or equal to 'target'
                ans = min(ans, r - l + 1)  # Update 'ans' with the minimum length found so far
                total -= nums[l]  # Subtract the element at 'l' from 'total'
                l += 1  # Move 'l' to the right

            r += 1  # Move 'r' to the right

        if ans == 10**18:  # If 'ans' remains unchanged (no subarray found)
            return 0  # Return 0
        return ans  # Otherwise, return 'ans'
