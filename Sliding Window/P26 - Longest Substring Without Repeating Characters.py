class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(min(m, n)), where m is the size of the character set
        
        # INTUITION:
        # We use a sliding window approach to find the longest substring without repeating characters.
        
        # ALGO:
        # 1. Initialize variables 'ans', 'l', 'r' to 0. 'ans' will hold the length of the longest substring found so far, 'l' and 'r' are pointers for the sliding window.
        # 2. Initialize an empty dictionary 'sCount' to store the count of characters in the current window.
        # 3. Loop through the string until 'r' reaches the end:
        #     3.1 While the character at 'r' is already in 'sCount':
        #         3.1.1 Decrement the count of the character at 'l' in 'sCount' and move 'l' to the right.
        #         3.1.2 If the count of the character at 'l' becomes 0, remove it from 'sCount'.
        #     3.2 Add the character at 'r' to 'sCount' with a count of 1.
        #     3.3 Update 'ans' with the maximum of its current value and the length of the current substring (r-l+1).
        #     3.4 Move 'r' to the right.
        # 4. Return 'ans'.
        
        ans, l, r = 0, 0, 0  # Initialize variables 'ans', 'l', 'r' to 0
        sCount = {}  # Initialize an empty dictionary 'sCount' to store character counts
        
        while r < len(s):  # Loop until 'r' reaches the end of the string
            while s[r] in sCount:  # While the character at 'r' is already in 'sCount'
                sCount[s[l]] -= 1  # Decrement the count of the character at 'l' in 'sCount'
                if sCount[s[l]] == 0:  # If the count of the character at 'l' becomes 0
                    sCount.pop(s[l])  # Remove it from 'sCount'
                l += 1  # Move 'l' to the right
            
            sCount[s[r]] = 1  # Add the character at 'r' to 'sCount' with a count of 1
            ans = max(ans, r - l + 1)  # Update 'ans' with the maximum of its current value and the length of the current substring
            r += 1  # Move 'r' to the right
            
        return ans  # Return 'ans'
