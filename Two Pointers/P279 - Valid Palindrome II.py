# Time Complexity:
# - O(N), where N is the length of the string
# - We scan through the string once with two pointers
# - When mismatch occurs, we do O(N) check for palindrome
# - Overall still O(N) as we only do palindrome check once

# Space Complexity:
# - O(N) to create substrings for palindrome check
# - Could be optimized to O(1) by checking palindrome in-place

# INTUITION:
# Since we can remove at most one character, we can:
# 1. Use two pointers to check if string is already palindrome
# 2. When we find a mismatch, we have two choices:
#    - Remove character at left pointer
#    - Remove character at right pointer
# 3. Check if either choice creates valid palindrome

# ALGORITHM:
# 1. Initialize two pointers at start and end
# 2. Move pointers inward while characters match
# 3. If mismatch found:
#    - Try skipping left character
#    - Try skipping right character
#    - Return true if either creates palindrome
# 4. Return true if we complete the check without mismatches

class Solution:
   def validPalindrome(self, s: str) -> bool:
       left = 0
       right = len(s) - 1
       
       while left < right:
           if s[left] == s[right]:
               left += 1
               right -= 1
           else:
               skipLeft = s[left:right]
               skipRight = s[left+1:right+1]
               return skipLeft == skipLeft[::-1] or skipRight == skipRight[::-1]
               
       return True
