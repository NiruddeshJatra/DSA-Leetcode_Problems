# Time Complexity: O(n log(sum - max))
# Space Complexity: O(1)

# INTUITION:
# The goal is to split the array `arr` into `k` subarrays such that the maximum sum of any subarray is minimized.
# This can be approached using binary search on the possible maximum subarray sums.
# The helper function `isPossible` checks if a given maximum subarray sum can be achieved with `k` or fewer subarrays.

# ALGO:
# 1. Define the helper function `isPossible`:
#    - Initialize `cntSplit` to 1 (indicating the first subarray) and `curSum` to 0.
#    - Iterate through the array:
#      - Add the current element to `curSum`.
#      - If `curSum` exceeds `total`, increment `cntSplit` and reset `curSum` to the current element.
#      - If `cntSplit` exceeds `k`, return False.
#    - Return True if the array can be split within the given constraints.
# 2. If the length of `arr` is less than `k`, return -1 (not enough elements to split).
# 3. Initialize the binary search bounds:
#    - `l` as the maximum element in the array (minimum possible maximum subarray sum).
#    - `r` as the sum of all elements in the array (maximum possible maximum subarray sum).
# 4. Perform binary search:
#    - Calculate the middle value `mid`.
#    - Use `isPossible` to check if `mid` is a feasible maximum subarray sum.
#    - If feasible, adjust the right bound `r` to `mid - 1` to find a smaller possible maximum.
#    - If not feasible, adjust the left bound `l` to `mid + 1` to find a larger possible maximum.
# 5. Return the left bound `l` as the smallest possible maximum subarray sum.



class Solution:
    def splitArray(self, arr: List[int], k: int) -> int:
        def isPossible(total):
            cntSplit, curSum = 1, 0
            for i in range(len(arr)):
                if curSum + arr[i] <= total:
                    curSum += arr[i]
                else:
                    cntSplit += 1
                    curSum = arr[i]
                if cntSplit > k:
                    return False
            return True

        if len(arr) < k:
            return -1
        l, r = max(arr), sum(arr)
        while l <= r:
            mid = (l + r) // 2
            if isPossible(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l

