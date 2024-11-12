# Time Complexity (T.C): O(n log(max_diff)), where n is the length of `nums`. The sorting operation takes O(n log n),
# and binary search over possible maximum differences has a complexity of O(log(max_diff)), where max_diff is the 
# difference between the max and min values in `nums`. For each mid in the binary search, we perform an O(n) scan of `nums`.

# Space Complexity (S.C): O(1), as we only use a constant amount of extra space.

# Intuition:
# This problem involves finding the minimum possible maximum difference between pairs in a list after selecting `p` pairs.
# By sorting `nums`, we ensure that consecutive differences between elements are minimized. Then, a binary search is used 
# to narrow down the smallest possible maximum difference (`mid`) that allows us to form `p` pairs with differences <= `mid`.
# This approach is efficient because binary search on a sorted array of possible differences allows us to avoid brute-force 
# enumeration of all pairs. The benefit is a significant time-saving by reducing the search space logarithmically.

# Algorithm:
# 1. Sort `nums` to allow for easy pair formation with minimal differences.
# 2. Set the search boundaries `l` (smallest difference) and `r` (largest difference).
# 3. Use binary search on this range: for each midpoint `mid`, attempt to form `p` pairs with differences <= `mid`.
# 4. Adjust `l` or `r` based on whether forming `p` pairs was successful, gradually converging to the minimum possible `mid`.
# 5. The binary search stops when `l` converges to the smallest feasible maximum difference.

# Code:
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        l, r = 0, nums[-1] - nums[0]
        while l < r:
            mid = (l + r) // 2
            pairsTaken = 0
            i = 1
            
            while i < len(nums):
                if nums[i] - nums[i - 1] <= mid:
                    pairsTaken += 1
                    i += 1
                    if pairsTaken == p:
                        break
                i += 1
            
            if pairsTaken >= p:
                r = mid
            else:
                l = mid + 1

        return l
