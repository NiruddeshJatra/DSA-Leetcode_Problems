from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        
        l, r = min(bloomDay), max(bloomDay)
        while l < r:
            mid = (l + r) // 2
            flower = bouq = 0
            
            for day in bloomDay:
                flower = 0 if day > mid else flower + 1
                if flower == k:
                    bouq += 1
                    flower = 0
                    if bouq == m:
                        break
            
            if bouq == m:
                r = mid
            else:
                l = mid + 1

        return l

# Time Complexity: O(n log d), where n is the number of days in bloomDay and d is the range of days between the minimum and maximum in bloomDay.
# Space Complexity: O(1), since we are using a constant amount of additional space.

# INTUITION:
# The problem requires us to determine the minimum number of days needed for `m` bouquets to be made, with each bouquet consisting of `k` consecutive flowers.
# To solve this, we use a binary search approach on the range of days, from the minimum day to the maximum day in bloomDay.
# The key insight is that if we can make `m` bouquets in `x` days, we can potentially make them in more than `x` days, but we need to find the smallest such `x`.

# ALGO:
# 1. INITIALIZE l (left) to the minimum day and r (right) to the maximum day in bloomDay.
# 2. While l is less than r:
#    2.1. Calculate mid, the midpoint of l and r.
#    2.2. Initialize flower and bouq to 0. flower counts consecutive flowers ready to bloom by day mid, and bouq counts bouquets formed.
#    2.3. For each day in bloomDay:
#        - Reset flower to 0 if the day is greater than mid.
#        - Otherwise, increment flower.
#        - If flower reaches k, increment bouq and reset flower to 0.
#        - If bouq reaches m, break out of the loop.
#    2.4. If bouq equals m, set r to mid to search for fewer days.
#    2.5. Otherwise, set l to mid + 1 to search for more days.
# 3. RETURN l, which is the minimum number of days needed to form m bouquets.

# EXPLANATION OF APPROACH:
# - Start by checking if it's possible to make m bouquets with k flowers each. If not, return -1.
# - Use binary search to efficiently narrow down the minimum number of days required.
# - For each midpoint day in the binary search, simulate the process of forming bouquets by iterating through bloomDay.
# - Count consecutive flowers that bloom by the midpoint day and form bouquets when k consecutive flowers are found.
# - Adjust the binary search range based on whether the required number of bouquets can be formed.
