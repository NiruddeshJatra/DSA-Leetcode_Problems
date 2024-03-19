# Time Complexity: O(n)
# Space Complexity: O(1)

# INTUITION:
# This function aims to find the maximum score that can be obtained by selecting 'k' cards from the array 'arr' 
# using a sliding window approach. It initializes a window of size 'k' at the beginning of the array and slides 
# it to the right while updating the total score. The maximum score encountered during this process is returned.

# ALGORITHM:
# 1. Initialize pointers 'l' and 'r' representing the left and right boundaries of the sliding window.
# 2. Calculate the initial total score by summing the values of the last 'k' elements of the array.
# 3. Initialize the answer 'ans' with the initial total score.
# 4. Slide the window to the right:
#    4.1 Update the total score by subtracting the value of the leftmost element and adding the value of the rightmost element.
#    4.2 Update the answer 'ans' with the maximum between the current 'ans' and the updated total score.
#    4.3 Move the window by incrementing both pointers 'l' and 'r'.
# 5. Return the maximum score 'ans'.

from typing import List

def maxPoints(arr: List[int], k: int) -> int:
    l, r = 0, len(arr) - k
    total = sum(arr[r:])
    ans = total
    while r < len(arr):
        total += arr[l] - arr[r]
        ans = max(ans, total)
        l += 1
        r += 1

    return ans
