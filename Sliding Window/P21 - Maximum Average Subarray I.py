class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        # INTUITION:
        # The idea is to calculate the average of the first k elements,
        # and then slide the window by one element at a time, updating the
        # average and keeping track of the maximum average seen so far.

        # ALGO:
        # 1. Initialize the average as the sum of the first k elements divided by k.
        # 2. Loop through the array starting from index k:
        #     2.1 Calculate the new average by subtracting the element going out of
        #         the window and adding the new element coming into the window.
        #     2.2 Update the maximum average if the new average is greater.
        # 3. Return the maximum average found.

        avg = (sum(nums[:k])) / k  # Initial average of first k elements
        ans = avg  # Initialize answer with initial average
        for i in range(k, len(nums)):  # Loop from k to end of nums
            avg = (avg * k + nums[i] - nums[i - k]) / k  # Slide the window and update average
            ans = max(ans, avg)  # Update maximum average if necessary
            
        return ans  # Return maximum average
