class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # Time Complexity: O(n*log(n)) - Sorting the array
        # Space Complexity: O(1) - Constant space
        
        # INTUITION:
        # This algorithm aims to find the maximum frequency of elements in the given list
        # with the constraint that at most k operations are allowed to change the elements.
        # It does so by maintaining a sliding window and adjusting it based on the given condition.
        
        # ALGORITHM:
        # 1. Sort the input list 'nums'.
        # 2. Initialize two pointers 'l' and 'r' to track the left and right ends of the window.
        # 3. Initialize variables 'res' to store the maximum frequency and 'total' to store the sum of elements in the window.
        # 4. Iterate through the elements using the right pointer 'r'.
        #     - Update 'total' by adding the current element.
        #     - While the current element multiplied by the length of the window is greater than 'total' plus 'k':
        #         - Update 'total' by subtracting the leftmost element of the window.
        #         - Move the left pointer 'l' to the right.
        #     - Update 'res' by taking the maximum of 'res' and the length of the current window.
        # 5. Return 'res' as the maximum frequency.
        
        nums.sort()  # Sorting the input list
        
        l, r = 0, 0  # Initializing pointers for the sliding window
        res, total = 0, 0  # Initializing variables to track frequency and window sum
        
        while r < len(nums):
            total += nums[r]  # Adding the current element to the window sum
            
            # Adjusting the window based on the given condition
            while nums[r] * (r - l + 1) > total + k:
                total -= nums[l]  # Removing the leftmost element from the window sum
                l += 1  # Moving the left pointer to the right
            
            res = max(res, r - l + 1)  # Updating the maximum frequency
            r += 1  # Moving the right pointer to the right
        
        return res  # Returning the maximum frequency
