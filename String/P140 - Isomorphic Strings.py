# Time Complexity: O(n) for the first solution, where n is the length of the strings `s` and `t`. 
# In each solution, we either traverse the strings linearly or perform constant-time operations for each character.
# Space Complexity: O(n) as we are using dictionaries to store mappings or lists to store character positions.

# INTUITION:
# The idea behind the isomorphism check is to ensure that:
# 1. Every character in string `s` can map to one and only one character in string `t`.
# 2. Every character in string `t` can map to one and only one character in string `s`.
# By using different strategies like dictionaries, character positions, and comparisons of their mappings, we can solve the problem efficiently.

# ALGO for the first solution:
# 1. Initialize two dictionaries, `s2t` and `t2s`, for tracking the mappings from `s` to `t` and `t` to `s` respectively.
# 2. Iterate through both strings and check:
#    - If the current character in `s` has already been mapped, it should map to the current character in `t`, otherwise return False.
#    - Similarly, check the reverse mapping from `t` to `s`.
# 3. If the mappings are consistent, return True, otherwise return False.

class Solution(object):
    # Solution 1: Using two dictionaries to track character mappings
    def isIsomorphic(self, s, t):
        # Step 1: Initialize two dictionaries
        s2t, t2s = {}, {}
        # Step 2: Iterate through the strings
        for i in range(len(s)):
            # Step 3: Check if the mapping from s to t is consistent
            if s[i] in s2t and s2t[s[i]] != t[i]:
                return False
            # Step 4: Check if the reverse mapping from t to s is consistent
            if t[i] in t2s and t2s[t[i]] != s[i]:
                return False
            # Step 5: Update the mappings
            s2t[s[i]] = t[i]
            t2s[t[i]] = s[i]
        # Step 6: Return True if all mappings are valid
        return True
    
    # Solution 2: Using character position lists
    def isIsomorphic2(self, s, t):
        # Step 1: Initialize two lists of lists to track character positions
        d1, d2 = [[] for _ in range(256)], [[] for _ in range(256)]
        # Step 2: Record the positions of each character in `s`
        for i, val in enumerate(s):
            d1[ord(val)].append(i)
        # Step 3: Record the positions of each character in `t`
        for i, val in enumerate(t):
            d2[ord(val)].append(i)
        # Step 4: Compare the sorted position lists
        return sorted(d1) == sorted(d2)
    
    # Solution 3: Using a set to check unique character pairs
    def isIsomorphic3(self, s, t):
        # Step 1: Check if the number of unique pairs in `s` and `t` is the same as the number of unique characters in `s` and `t`
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
    
    # Solution 4: Using index comparisons
    def isIsomorphic4(self, s, t): 
        # Step 1: Compare the index positions of each character's first appearance in `s` and `t`
        return [s.find(i) for i in s] == [t.find(j) for j in t]
    
    # Solution 5: Using map and find
    def isIsomorphic5(self, s, t):
        # Step 1: Use map and find to compare the positions of each character's first appearance
        return list(map(s.find, s)) == list(map(t.find, t))
