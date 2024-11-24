# Time Complexity: O(n), where n is the length of the strings `s` and `t`.  
# - Splitting `s` and `t` into substrings takes O(n).  
# - Counting substrings using `Counter` also takes O(n).  
# - Comparing the two counters takes O(k), where k is the number of unique substrings, but k is generally much smaller than n.  

# Space Complexity: O(k), where k is the number of unique substrings of length `length = len(s) // k`.  
# - We store the frequency counts of substrings for both `s` and `t`.  

# INTUITION:  
# The task is to determine if it's possible to rearrange the string `s` into string `t` by dividing both strings into k equal parts.  
# To solve this, the problem boils down to ensuring that both strings can be divided into the same set of substrings, with the same frequencies.  
# - Split both strings `s` and `t` into `k` equal parts.  
# - Use a `Counter` to calculate the frequency of each substring in both strings.  
# - Compare the two counters; if they are equal, it means `s` can be rearranged into `t`.  

# ALGORITHM:  
# 1. Calculate the length of each substring as `len(s) // k`.  
# 2. Split `s` and `t` into k substrings of the calculated length.  
# 3. Use `Counter` to compute the frequency of each substring in `s` and `t`.  
# 4. Compare the two counters.  
# 5. If they are equal, return `True`; otherwise, return `False`.

from collections import Counter

class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        # Calculate the length of each substring
        substringLength = len(s) // k
        
        # Create frequency counters for substrings of s and t
        sSubstringCount = Counter(s[i:i + substringLength] for i in range(0, len(s), substringLength))
        tSubstringCount = Counter(t[i:i + substringLength] for i in range(0, len(t), substringLength))
        
        # Compare the two counters
        return sSubstringCount == tSubstringCount


# Example Usage:
# solution = Solution()
# s = "aabbcc"
# t = "bbaacc"
# k = 3
# print(solution.isPossibleToRearrange(s, t, k))  # Example Output: True
