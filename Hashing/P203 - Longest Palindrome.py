# Time Complexity: O(n), where n is the length of the input string `s`.  
# - The `Counter` operation iterates through the string once to calculate the frequency of each character, which takes O(n).  
# - The iteration over the items in the frequency dictionary also takes O(n) in total since the sum of all frequencies equals n.  
# Hence, the overall complexity is O(n).

# Space Complexity: O(1) (technically O(c), where c is the number of unique characters in `s`).  
# - The `Counter` data structure uses space proportional to the number of unique characters in the string.  
# - For the standard ASCII set, the maximum unique characters are fixed at 128, making the space usage effectively O(1).  

# INTUITION:  
# The task is to find the length of the longest palindrome that can be formed using the characters of the input string.  
# A palindrome requires that characters have even frequencies, except for at most one character, which can have an odd frequency (and occupy the middle of the palindrome).  
# By summing up the even frequencies and reducing odd frequencies by 1 (making them even), we can calculate the length of the longest possible palindrome.  
# If any odd frequency exists, we can add 1 to the result to account for a single odd character in the middle of the palindrome.

# ALGO:  
# 1. Count the frequency of each character in the string using the `Counter` class.  
# 2. Initialize `ans` to 0 to keep track of the length of the palindrome, and `oddCnt` as a flag to track the presence of odd frequencies.  
# 3. Iterate over the frequency dictionary:  
#    - If a character's frequency is even, add it directly to `ans`.  
#    - If a character's frequency is odd, add `count - 1` to `ans` (making it even) and set `oddCnt` to True.  
# 4. If `oddCnt` is True, add 1 to `ans` to account for one odd character in the middle of the palindrome.  
# 5. Return `ans`.

from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Count the frequency of each character
        freq = Counter(s)
        ans = 0
        oddCnt = False  # Flag to track the presence of odd frequencies

        # Iterate over the frequencies
        for char, count in freq.items():
            if count % 2 == 1:  # Odd frequency
                oddCnt = True
                ans += count - 1  # Add the largest even part
            else:  # Even frequency
                ans += count

        # Add 1 to the result if there was an odd frequency
        return ans if not oddCnt else ans + 1
