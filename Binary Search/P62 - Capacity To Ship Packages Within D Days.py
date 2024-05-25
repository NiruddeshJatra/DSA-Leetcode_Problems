from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        while l < r:
            mid = (l + r) // 2
            load, daysRequired = 0, 0
            for i in weights:
                load += i
                if load > mid:
                    load = i
                    daysRequired += 1

            daysRequired += 1    
            if daysRequired > days:
                l = mid + 1
            else:
                r = mid

        return r

# Time Complexity: O(n log S), where n is the number of weights and S is the sum of weights.
# Space Complexity: O(1), since we are using a constant amount of additional space.

# INTUITION:
# The problem requires us to find the minimum capacity of the ship such that we can ship all packages within a given number of days.
# Using binary search on the range of possible capacities (from the maximum weight to the sum of all weights) allows us to efficiently determine the smallest capacity that meets the requirement.
# The key insight is that for each midpoint capacity, we can simulate the shipping process and count the number of days required to ship all packages.

# ALGO:
# 1. INITIALIZE l (left) to max(weights) (smallest possible capacity) and r (right) to sum(weights) (largest possible capacity).
# 2. While l is less than r:
#    2.1. Calculate mid, the midpoint of l and r.
#    2.2. Initialize load to 0 and daysRequired to 0.
#    2.3. For each weight i in weights:
#        - Add i to load.
#        - If load exceeds mid, increment daysRequired and reset load to i.
#    2.4. Increment daysRequired by 1 to account for the last shipment.
#    2.5. If daysRequired exceeds the given days, set l to mid + 1, meaning mid is too small a capacity.
#    2.6. Otherwise, set r to mid, meaning mid is a valid capacity, but we try for a smaller one.
# 3. RETURN r, which will be the minimum capacity that allows us to ship all packages within the given days.

# EXPLANATION OF APPROACH:
# - We start by setting the binary search bounds between the maximum weight (smallest possible capacity) and the sum of all weights (largest possible capacity).
# - We iteratively calculate the midpoint and check if it can be a valid capacity by simulating the shipping process.
# - For each midpoint capacity, we count the number of days required to ship all packages by incrementally adding weights to the load.
# - If the load exceeds the midpoint capacity, we increment the days required and reset the load to the current weight.
# - If the total days required exceeds the given days, we need a larger capacity, so we adjust the left bound.
# - If the total days required is within the given days, we adjust the right bound to try finding a smaller valid capacity.
# - This process continues until the left and right bounds converge, giving us the smallest capacity that satisfies the condition.
