# Time Complexity: O(n), where n is the size of the input array `arr`.
# Space Complexity: O(1)

# INTUITION:
# We are using a sliding window approach to find the longest subarray with at most `k` zeros.
# The window starts from the left index `l` and expands to the right index `r`.
# We keep track of the number of zeros encountered (`zeroCount`) and adjust the window accordingly.
# At each step, we update the answer with the maximum length of the valid subarray.

# ALGORITHM:
# 1. Initialize variables `l` (left pointer), `ans` (answer), and `zeroCount` (count of zeros) to 0.
# 2. Iterate through the array using a sliding window approach:
#    - Increment `zeroCount` when encountering a zero.
#    - Adjust the window by incrementing `l` until the number of zeros in the window is less than or equal to `k`.
#    - Update `ans` with the maximum length of the valid subarray.
# 3. Return `ans`.

class Solution:
    def longestOnes(self, arr: List[int], k: int) -> int:
        l, ans = 0, 0
        zeroCount = 0
        for r in range(len(arr)):
            if arr[r] == 0:
                zeroCount += 1

            while zeroCount > k:
                if arr[l] == 0:
                    zeroCount -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans
