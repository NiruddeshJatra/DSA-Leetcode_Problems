class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        # INTUITION:
        # This algorithm aims to find the minimum window in 's' which contains 
        # all the characters of string 't'. It iterates through 's' using a 
        # sliding window approach, adjusting the left and right pointers 
        # to minimize the window size while maintaining the required characters 
        # from 't' within the window.
        
        # ALGO:
        # 1. Initialize a dictionary 'tCount' to count the occurrences of each 
        #    character in string 't'.
        # 2. Initialize variables 'l' (left pointer) and 'ans' to represent 
        #    the start index and the minimum window respectively.
        # 3. Iterate through each character in 's' using the right pointer 'r'.
        #    3.1. If the character at 's[r]' is in 't', decrement its count 
        #         in 'tCount'. If the count becomes zero or negative, decrement 
        #         'tLength', which keeps track of the remaining characters 
        #         required from 't' to form the window.
        #    3.2. While 'tLength' becomes zero (indicating all characters from 
        #         't' are present in the window):
        #         - Update 'ans' if the current window size is smaller than the 
        #           previous minimum window size.
        #         - Increment 'l' to shrink the window size from the left.
        #         - If the character at 's[l]' is in 't', increment its count 
        #           in 'tCount'. If the count becomes positive, increment 
        #           'tLength' to indicate the character is required to form 
        #           the window.
        # 4. Return 'ans', which represents the minimum window containing all 
        #    characters from 't'.

        tCount = {}
        for c in t:
            tCount[c] = 1 + tCount.get(c, 0)
            
        l = 0
        ans = ""
        tLength = len(t)
        
        for r in range(len(s)):
            if s[r] in tCount:
                tCount[s[r]] -= 1
                if tCount[s[r]] >= 0:
                    tLength -= 1
                              
            while tLength == 0:
                if not ans or len(ans) > (r - l + 1):
                    ans = s[l:r + 1]
                
                if s[l] in tCount:
                    tCount[s[l]] += 1
                    if tCount[s[l]] > 0:
                        tLength += 1
                    
                l += 1
                
        return ans
