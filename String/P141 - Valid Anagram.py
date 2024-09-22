# Time Complexity: O(n), where n is the length of the strings `s` and `t`. We iterate through both strings once, which takes linear time.
# Space Complexity: O(n), as we are using a dictionary to store the frequency counts of characters, which in the worst case can store all unique characters.

# INTUITION:
# The idea is to check if the two strings `s` and `t` are anagrams of each other. 
# Two strings are anagrams if they contain the same characters with the same frequencies.
# We can solve this by counting the frequency of characters in `s` and checking if the frequencies match in `t`.

# ALGO:
# 1. Use a dictionary `count` to track the frequency of characters in `s`.
# 2. Iterate over `s` and increment the count of each character in the dictionary.
# 3. Iterate over `t` and decrement the count of each character.
# 4. Finally, check if all values in the dictionary are zero, which would mean the two strings have matching character frequencies.
# 5. If any value is not zero, return False, indicating the strings are not anagrams. Otherwise, return True.

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step 1: Initialize a defaultdict to track character counts
        count = defaultdict(int)
        
        # Step 2: Count the frequency of characters in string `s`
        for x in s:
            count[x] += 1
        
        # Step 3: Decrement the frequency of characters in string `t`
        for x in t:
            count[x] -= 1
        
        # Step 4: Check if any character has a non-zero frequency
        for val in count.values():
            if val != 0:
                return False
        
        # Step 5: If all counts are zero, the strings are anagrams
        return True
