# Time Complexity: O(n log m), where n is the number of piles and m is the maximum number of bananas in a pile.
# Space Complexity: O(1), as we are using a constant amount of additional space.

# INTUITION:
# The problem is to determine the minimum eating speed (k) such that all the bananas can be eaten within h hours.
# Using binary search helps us efficiently narrow down the possible values for k.
# By checking how long it takes to eat all the bananas at different speeds, we can find the smallest feasible speed.

# ALGO:
# 1. INITIALIZE l (left) to 1 (minimum possible speed) and r (right) to max(piles) (maximum possible speed).
# 2. While l is less than or equal to r:
#    2.1. Calculate mid, the average of l and r.
#    2.2. Initialize time to 0.
#    2.3. For each pile in piles, add the time required to finish that pile at speed mid to time.
#    2.4. If time exceeds h, it means mid is too slow, so update l to mid + 1.
#    2.5. Otherwise, update ans to the minimum of mid and ans, and update r to mid - 1.
# 3. RETURN ans, which holds the minimum eating speed that allows Koko to finish all bananas within h hours.


import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = r
        while l <= r:
            mid = (l + r) // 2
            time = 0
            for i in piles:
                time += math.ceil(i / mid)
            if time > h:
                l = mid + 1
            else:
                ans = min(mid, ans)
                r = mid - 1

        return ans

