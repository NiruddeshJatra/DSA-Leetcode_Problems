# Time Complexity: O(log n), where n is the number of versions.
# Space Complexity: O(1), as the algorithm uses a constant amount of extra space.

# INTUITION:
# The problem involves finding the first bad version in a range of versions from 1 to n. We can approach this problem 
# using binary search efficiently.
# 
# **Binary Search Approach**: The key observation is that the versions are sorted. We can use binary search to 
# efficiently find the first bad version.
# 
# **Understanding Binary Search**: In each step of binary search, we check the middle version. If the middle version 
# is bad, we know that all versions after it must also be bad. Therefore, we adjust the search range to the left half. 
# If the middle version is not bad, we know that all versions before it must be good. Therefore, we adjust the search 
# range to the right half.
# 
# **Finding the First Bad Version**: We continue this process until we find the first bad version. When the search 
# range reduces to a single version, it must be the first bad version. We return this version as the result.

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
