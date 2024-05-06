# Time Complexity: O(log n), where n is the number of elements in the 'letters' list.
#                    This is because binary search is utilized to find the next greatest letter.
# Space Complexity: O(1), as the algorithm uses a constant amount of extra space.

# INTUITION:
# The problem asks to find the smallest letter in the list that is larger than the given target letter. 
# To efficiently find this, we utilize binary search.

# ALGO:
# 1.  Initialize pointers 'l' and 'r' to the start and end of the 'letters' list, respectively.
# 2.  Perform binary search:
#     2.1 If the middle element is greater than the target letter, update 'r' to mid - 1.
#     2.2 Otherwise, update 'l' to mid + 1.

# RETURN letters[l % len(letters)]

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target < letters[0] or target >= letters[-1]:
            return letters[0]
        
        l, r = 0, len(letters) - 1
        while l <= r:
            mid = (l + r) // 2
            if letters[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return letters[l % len(letters)]
