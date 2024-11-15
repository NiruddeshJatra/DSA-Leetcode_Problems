# Time Complexity: O(n), where n is the length of nums.  
# The algorithm traverses the array once, and dictionary operations (insertions and lookups) are O(1).

# Space Complexity: O(min(n, k)).  
# The dictionary `hashmap` can hold up to `k` elements in the worst case, making the space usage proportional to the window size.

# INTUITION:
# The problem is to determine whether there are two indices `i` and `j` such that `nums[i] == nums[j]` and the absolute difference `|i - j| <= k`.  
# A dictionary (`hashmap`) allows us to efficiently store the last seen index of each element.  
# By keeping track of the most recent index of each number, we can check in constant time if a duplicate exists within the allowable distance `k`.  
# This approach avoids nested loops, ensuring a linear time complexity, and uses a sliding window-like mechanism conceptually.

# ALGO:
# 1. Initialize an empty dictionary `hashmap` to store the last seen index of each number in `nums`.
# 2. Iterate through the array:
#    - If the current number is in `hashmap` and the difference between the current index `i` and the last seen index stored in `hashmap` is less than or equal to `k`, return `True`.
#    - Update the dictionary with the current index of the number.
# 3. If no such pair is found after the loop, return `False`.

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap and i - hashmap[nums[i]] <= k:
                return True
            hashmap[nums[i]] = i
        
        return False
