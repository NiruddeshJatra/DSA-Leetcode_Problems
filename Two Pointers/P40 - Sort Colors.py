# Time Complexity: O(n)
# Space Complexity: O(1)

# INTUITION:
# This function sorts an array 'nums' containing only 0, 1, and 2 in ascending order using the Dutch National Flag algorithm.
# It maintains three pointers: 'red', 'white', and 'blue'. The 'red' pointer indicates the boundary of the red (0) region,
# the 'white' pointer indicates the boundary of the white (1) region, and the 'blue' pointer indicates the boundary of the blue (2) region.
# As the 'white' pointer moves through the array, it swaps elements to group 0s, 1s, and 2s accordingly.

# ALGORITHM:
# 1. Initialize three pointers: 'red' pointing to the start of the array (0), 'white' pointing to the start of the array (0),
#    and 'blue' pointing to the end of the array (len(nums) - 1).
# 2. While the 'white' pointer is less than or equal to the 'blue' pointer:
#    2.1 If the element at 'white' is 0, swap it with the element at 'red' and increment both 'red' and 'white'.
#    2.2 If the element at 'white' is 1, increment 'white'.
#    2.3 If the element at 'white' is 2, swap it with the element at 'blue' and decrement 'blue'.
# 3. The array 'nums' will be sorted in place after the execution of the algorithm.

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red, white, blue = 0, 0, len(nums) - 1
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
