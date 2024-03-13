class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        
        # INTUITION:
        # This algorithm aims to find the length of the longest substring 
        # that can be formed by replacing at most 'k' characters with any other character.
        # The approach involves using a sliding window technique to maintain a window 
        # with the maximum frequency character and keeping track of the count of 
        # characters to be replaced.
        
        # ALGO:
        # 1. Initialize variables: l and r to represent the left and right pointers 
        #    of the sliding window, maxf to store the maximum frequency of any character 
        #    within the window, ans to store the length of the longest valid substring, 
        #    and freq dictionary to store the frequency of characters within the window.
        # 2. Iterate through each character in the string using the right pointer (r).
        #    2.1. Update the frequency of the current character in the freq dictionary 
        #         and update maxf if necessary.
        #    2.2. Check if the length of the current window minus maxf is greater than 'k'.
        #        If so, move the left pointer (l) and update the frequency of the character 
        #        at the left pointer. Repeat this step until the window becomes valid.
        #    2.3. Update ans with the maximum length seen so far.
        #    2.4. Move the right pointer (r) to expand the window.
        # 3. Return ans which represents the length of the longest valid substring.
        
        l, r = 0, 0
        maxf, ans = 0, 0
        freq = {}
        
        while r < len(s):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            maxf = max(maxf, freq[s[r]])
            
            while (r-l+1) - maxf > k:
                freq[s[l]] -= 1
                l += 1
                
            ans = max(ans, r - l + 1)
            r += 1
            
        return ans
