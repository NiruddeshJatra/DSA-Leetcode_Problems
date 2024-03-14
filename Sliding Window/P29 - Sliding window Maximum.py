from typing import List
import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Time Complexity: O(n)
        # Space Complexity: O(k)
        
        # INTUITION:
        # This algorithm aims to find the maximum value in each sliding window 
        # of size 'k' within the given list 'nums'.
        # The approach involves using a deque (double-ended queue) to store indices 
        # of elements in the current window. At each step, we maintain the deque 
        # such that it stores only the indices of elements in the current window 
        # and elements in descending order of their values.
        
        # ALGO:
        # 1. Initialize an empty list 'ans' to store the maximum values of each window,
        #    and a deque 'q' to maintain the indices of elements in the current window.
        # 2. Iterate through each index 'r' in the range of the length of 'nums'.
        #    2.1. While 'q' is not empty and the current element 'nums[r]' is greater 
        #         than the value at the index 'q[-1]' (rightmost element in 'q'), 
        #         pop elements from 'q' until 'nums[r]' is not greater than the 
        #         value at 'q[-1]'.
        #    2.2. Append the index 'r' to 'q'.
        #    2.3. If the leftmost index 'l' is greater than the leftmost index in 'q',
        #         pop the leftmost index from 'q' until 'l' is not greater than 
        #         the leftmost index in 'q'.
        #    2.4. If the current index 'r' has reached a position where the window 
        #         size is 'k', append the maximum value from the current window 
        #         (the value at index 'q[0]') to 'ans'.
        #    2.5. Increment 'l' to move the window forward.
        # 3. Return 'ans'.
        
        ans = []
        q = collections.deque()
        l = 0
        
        for r in range(len(nums)):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
                
            q.append(r)
            
            if l > q[0]:
                q.popleft()
            
            if r >= k - 1:
                ans.append(nums[q[0]])
                l += 1
            
        return ans
