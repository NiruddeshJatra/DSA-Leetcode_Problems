# Time Complexity: O(n^2), where n is the length of the string `s`. 
# We iterate over all substrings, and for each substring, we compute the difference 
# between the maximum and minimum frequency of characters in O(1) time using a frequency map.

# Space Complexity: O(1), since the frequency dictionary stores at most 26 characters 
# (constant space for the English alphabet).

# INTUITION:
# The problem asks for the beauty sum of all substrings of a given string `s`. 
# The beauty of a substring is defined as the difference between the maximum and minimum frequency 
# of any character in that substring.
# To calculate this efficiently, we maintain a frequency map for each starting point 
# and update it as we extend the substring.

# ALGO:
# 1. Initialize a variable `ans` to store the total beauty sum of all substrings.
# 2. Iterate over each possible starting point `i` of the substring.
# 3. For each starting point `i`, initialize a frequency dictionary `freq` to store the character counts.
# 4. Iterate over each ending point `j` for the substring starting at `i` and update the frequency of characters.
# 5. For each substring, compute the beauty by finding the difference between the maximum and minimum frequency 
#    (ignoring characters with zero frequency).
# 6. Add the beauty of the substring to `ans`.
# 7. Return `ans` as the final result.

class Solution:
    def beautySum(self, s: str) -> int:
        ans = 0
        
        # Iterate over each starting point of the substring
        for i in range(len(s)):
            freq = {}  # Frequency dictionary to store character counts
            # Iterate over each ending point for the substring starting at `i`
            for j in range(i, len(s)):
                freq[s[j]] = freq.get(s[j], 0) + 1  # Update frequency of current character
                
                # Compute the beauty of the current substring
                max_freq = max(freq.values())
                min_freq = min(x for x in freq.values() if x)  # Ignore characters with zero frequency
                
                # Add the beauty to the total sum
                ans += max_freq - min_freq
        
        return ans  # Return the total beauty sum of all substrings
