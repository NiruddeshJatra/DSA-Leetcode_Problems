# Time Complexity: O(n * k * log(k)), where `n` is the number of strings in `strs`, and `k` is the average length of a string.  
# - Sorting each string takes O(k * log(k)), and we do this for `n` strings.  
# - Inserting into and retrieving from the dictionary are O(1) operations on average.  
# - Total complexity: O(n * k * log(k)).

# Space Complexity: O(n * k), where `n` is the number of strings and `k` is the average length of a string.  
# - The dictionary `anagramMap` stores each string in its corresponding group, requiring O(n * k) space.  
# - Additionally, space is used for temporary storage of sorted strings, which is negligible compared to the dictionary.

# INTUITION:  
# The task is to group words that are anagrams of each other.  
# An anagram can be uniquely identified by sorting its characters.  
# For example, "eat", "tea", and "ate" all become "aet" when sorted.  
# Using this property:  
# 1. We sort each word to form a key.  
# 2. All words that are anagrams of each other will share the same sorted key.  
# 3. Grouping words under these keys in a dictionary results in the desired grouping.

# ALGORITHM:  
# 1. Create a `defaultdict` to group words sharing the same sorted key.  
# 2. Iterate through each word in `strs`:  
#    - Sort the characters of the word to create a key.  
#    - Append the word to the list corresponding to this key in the dictionary.  
# 3. Convert the dictionary's values to a list and return it.

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to group anagrams
        anagramMap = defaultdict(list)

        # Process each word in the input
        for word in strs:
            # Generate the sorted key
            sortedKey = ''.join(sorted(word))
            # Group the word by its sorted key
            anagramMap[sortedKey].append(word)

        # Return grouped anagrams as a list of lists
        return list(anagramMap.values())
