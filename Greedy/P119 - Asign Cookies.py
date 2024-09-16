# Time Complexity: O(n log n + m log m), where n is the length of `g` (children's greed array) and m is the length of `s` (cookies array). Sorting both arrays takes O(n log n) and O(m log m) respectively, and the while loop runs in O(n + m).
# Space Complexity: O(1), as we are using only a constant amount of extra space.

# INTUITION:
# The goal is to maximize the number of content children by giving them cookies. Each child `i` has a greed factor `g[i]`, and each cookie `j` has a size `s[j]`. A child is content if they get a cookie of size greater than or equal to their greed.
#
# **Key Insight**:
# - By sorting both the children's greed array (`g`) and the cookies array (`s`), we can use a two-pointer approach to try to assign the smallest possible cookie to each child, moving through both arrays greedily.

# ALGO:
# 1. **Sort the Arrays**:
#    - Sort the greed array `g` and the size array `s` in non-decreasing order.
# 2. **Two-Pointer Approach**:
#    - Initialize two pointers `i` and `j` to 0, where `i` tracks the current child and `j` tracks the current cookie.
# 3. **Traverse and Match Cookies**:
#    - While both `i` and `j` are within their respective array bounds:
#        - If the current cookie `s[j]` is large enough to satisfy the greed of the current child `g[i]` (i.e., `s[j] >= g[i]`), move to the next child by incrementing `i`.
#        - In either case, move to the next cookie by incrementing `j`.
# 4. **Return the Number of Content Children**:
#    - When the loop ends, `i` will represent the number of content children since it tracks how many children have been satisfied.

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Step 1: Sort the greed factors and the cookie sizes
        g.sort()
        s.sort()

        # Step 2: Initialize pointers for the children and cookies
        i, j = 0, 0

        # Step 3: Traverse both arrays to find the maximum number of content children
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                # If the current cookie satisfies the current child's greed, move to the next child
                i += 1
            # In either case, move to the next cookie
            j += 1
        
        # Step 4: Return the number of content children
        return i
