# Time Complexity:
# - O(N) where N is length of customers array
#   - Single pass through array using sliding window
#   - Each element processed exactly once

# Space Complexity:
# - O(1), using only variables for tracking
#   - No additional data structures needed
#   - Not modifying input arrays

# INTUITION:
# To maximize satisfied customers:
# - Some customers already satisfied (grumpy[i] = 0)
# - Can make owner not grumpy for minutes window
# Use sliding window to find optimal minutes where:
# - Track already satisfied outside window
# - Track turned satisfied within window
# Maximum is sum of these two groups

# ALGO:
# 1. Use sliding window, for each position:
#    - If not grumpy, add to alreadySatisfied
#    - If grumpy, add to currentTurnedSatisfied
#    - Maintain window of size minutes:
#      * Remove leftmost if grumpy
#    - Track maximum turned satisfied
# 2. Return sum of already + max turned

class Solution:
   def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
       # Initialize tracking variables
       left = maxTurnedSatisfied = currentTurnedSatisfied = alreadySatisfied = 0
       
       # Process each position
       for right in range(len(customers)):
           # Track satisfied customers
           if grumpy[right] == 0:
               alreadySatisfied += customers[right]
           else:
               currentTurnedSatisfied += customers[right]
               
           # Maintain window size
           if right - left + 1 > minutes:
               currentTurnedSatisfied -= (grumpy[left] * customers[left])
               left += 1
               
           # Update maximum turned satisfied
           maxTurnedSatisfied = max(maxTurnedSatisfied, currentTurnedSatisfied)
           
       return alreadySatisfied + maxTurnedSatisfied
