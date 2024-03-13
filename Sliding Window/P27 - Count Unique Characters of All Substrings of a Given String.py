class Solution:
    def uniqueLetterString(self, s: str) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        
        # INTUITION:
        # This algorithm aims to calculate the number of unique substrings that can be formed 
        # with the given string 's', where each substring contains only one unique character. 
        # The approach involves keeping track of the positions of each character in the string 
        # and calculating the contribution of each character to the total count of unique substrings.
        
        # ALGO:
        # 1. Initialize variables: ans to store the total count of unique substrings, 
        #    stepCount to track the contribution of each character, and last to store 
        #    the last occurrence indices of characters.
        # 2. Iterate through each character and its index in the string.
        #    2.1. If the character is encountered for the first time, initialize its 
        #         last occurrence indices in last dictionary.
        #    2.2. If the character is encountered again, update the stepCount by subtracting 
        #         the distance between the previous and current occurrences from stepCount.
        #    2.3. Update the last occurrence indices in the last dictionary.
        #    2.4. Update the stepCount by adding the distance between the previous and current 
        #         occurrences of the character.
        #    2.5. Update the ans by adding the current stepCount to it.
        # 3. Return the ans which represents the total count of unique substrings.
        
        ans, stepCount = 0, 0
        last = {}
        
        for i, c in enumerate(s):
            if c not in last:
                last[c] = [-1, i]
            else:
                stepCount -= last[c][1] - last[c][0]
                last[c] = [last[c][1], i]
            stepCount += last[c][1] - last[c][0]
            ans += stepCount
            
        return ans
