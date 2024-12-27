# Time Complexity:
# - O(N) where N is length of nums array
#   - Single pass through array: O(N)
#   - Each element enters and leaves deque at most once
#   - All deque operations (append/pop from both ends) are O(1)

# Space Complexity:
# - O(k) for the deque
#   - Deque stores at most k elements at any time
#   - Each element is a pair of (score, index)

# INTUITION:
# This is a dynamic programming problem with sliding window maximum:
# - At each index i, we want max score possible jumping from previous k positions
# - We can use a monotonic decreasing deque to track maximum scores
# - Deque maintains scores in decreasing order and removes outdated scores
# - Front of deque always contains maximum score from last k positions
# Monotonic deque gives us O(1) access to max in sliding window

# ALGO:
# 1. Initialize deque with first score and index
# 2. For each position i in range(1, n):
#    - Remove outdated scores (indices < i-k) from front
#    - Calculate current score using max from deque (front)
#    - Remove smaller scores from back (they can't be future maximums)
#    - Add current score and index to deque
# 3. Return final score (last element in deque)

class Solution:
   def maxResult(self, nums: List[int], k: int) -> int:
       # Initialize deque with first element
       dq = deque([(nums[0], 0)])
       
       # Process remaining elements
       for i in range(1, len(nums)):
           # Remove outdated scores from front
           while dq and dq[0][1] < (i-k):
               dq.popleft()
           
           # Calculate current score using maximum from previous window
           score = dq[0][0] + nums[i]
           
           # Remove smaller scores from back (maintain monotonic decreasing)
           while dq and dq[-1][0] <= score:
               dq.pop()
           
           # Add current score and index
           dq.append([score, i])
       
       # Return final maximum score
       return dq[-1][0]
