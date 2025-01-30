# Time Complexity:
# - O(N), where N is length of secret/guess strings
# - Two passes through strings: one for bulls, one for cows
# - Counter creation is O(N)

# Space Complexity:
# - O(K) where K is size of character set (digits 0-9)
# - Counter dictionary stores frequency of digits

# INTUITION:
# First count exact matches (bulls), then count digits that match
# but are in wrong positions (cows). Need to track remaining digits 
# with Counter to avoid double counting. Format result as "xAyB".

# ALGO:
# 1. Create Counter for secret string digits
# 2. First pass: count bulls (exact matches)
#    - Decrement counter for matched digits
# 3. Second pass: count cows (digit matches in wrong position)
#    - Only count if digit exists in counter and wasn't bull
#    - Decrement counter for used digits
# 4. Return formatted string with bulls and cows

class Solution:
   def getHint(self, secret: str, guess: str) -> str:
       digitCount = Counter(secret)
       bullCount = cowCount = 0
       
       # First pass: count bulls (exact matches)
       for i in range(len(secret)):
           if secret[i] == guess[i]:
               bullCount += 1
               digitCount[secret[i]] -= 1
               
       # Second pass: count cows (digit matches in wrong position)
       for i in range(len(secret)):
           currentDigit = guess[i]
           if (currentDigit in digitCount and 
               secret[i] != guess[i] and 
               digitCount[currentDigit] > 0):
               cowCount += 1
               digitCount[currentDigit] -= 1
               
       return f'{bullCount}A{cowCount}B'
