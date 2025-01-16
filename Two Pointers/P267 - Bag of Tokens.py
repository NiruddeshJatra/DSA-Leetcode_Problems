# Time Complexity:
# - O(N log N) for sorting tokens array
# - O(N) for processing tokens with two pointers
# - Total: O(N log N) where N is number of tokens

# Space Complexity:
# - O(1) as we only use constant extra space
# - Sort may use O(log N) space depending on implementation

# INTUITION:
# To maximize score, we should:
# 1. Play lowest tokens face-up to gain score efficiently
# 2. Play highest tokens face-down when we need more power
# Two pointer approach is optimal because:
# - Sort lets us easily access min/max tokens
# - Left pointer tracks smallest unplayed tokens
# - Right pointer tracks largest unplayed tokens
# - Can greedily choose best move at each step

# ALGORITHM:
# 1. Sort tokens in ascending order
# 2. Handle base cases (empty array or can't play first token)
# 3. Play first token face-up to start with score 1
# 4. Use two pointers to track remaining tokens
# 5. While tokens remain (i <= j):
#    - If can't play next smallest token:
#      * Play largest token face-down if possible
#      * Decrement score, gain power
#    - If can play next smallest token:
#      * Play it face-up
#      * Increment score, lose power

class Solution:
   def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
       # Sort tokens to enable two-pointer approach
       tokens.sort()
       
       # Handle base cases
       if not tokens or power < tokens[0]:
           return 0
           
       # Play first token to start with score 1
       power -= tokens[0]
       currentScore = 1
       
       # Initialize two pointers
       leftPtr = 1  # Next smallest token
       rightPtr = len(tokens) - 1  # Largest remaining token
       
       while leftPtr <= rightPtr:
           if power < tokens[leftPtr]:
               # Can't play next token face-up
               if leftPtr != rightPtr:
                   # Play largest token face-down if we have multiple tokens
                   power += tokens[rightPtr]
                   currentScore -= 1
               rightPtr -= 1
               
           else:
               # Play next smallest token face-up
               power -= tokens[leftPtr]
               currentScore += 1
               leftPtr += 1
               
       return currentScore
