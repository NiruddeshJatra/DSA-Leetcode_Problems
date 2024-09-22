# Time Complexity: O(n * m * log(n)), where n is the number of strings in the input list `strs`, and m is the average length of the strings.
# - Sorting the strings takes O(n * log(n)).
# - Comparing characters of strings in the inner loop takes O(n * m) in the worst case, where m is the length of the shortest string.

# Space Complexity: O(n), due to the space used for storing the sorted version of the input strings and intermediate variables.

# INTUITION:
# The problem is to find the longest common prefix shared by all strings in the input list. 
# We can solve this by sorting the strings and comparing their prefixes since the shortest string will determine the maximum possible length of the prefix.
# After sorting, the common prefix must be a prefix of the first and last strings in the sorted array, as these will differ the most.

# ALGO:
# 1. First, handle edge cases where the input list is empty or contains only one string.
# 2. Sort the list of strings by length (since the shortest string determines the maximum possible length of the prefix).
# 3. Initialize a variable to track the length of the longest common prefix.
# 4. For each consecutive pair of strings in the sorted list, compare their characters to find the common prefix length.
# 5. Update the length of the common prefix each time by taking the minimum prefix length found so far.
# 6. Return the common prefix based on the length calculated.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Edge cases: empty list or list with only one string
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        # Step 1: Sort the list of strings by length
        s = sorted(list(set(strs)), key=lambda x: len(x))
        
        # Step 2: Initialize variables
        if s[0] == "":
            return s[0]  # Return an empty string if the shortest string is empty
        
        i = 1
        length = float('inf')  # Initialize length as infinity
        
        # Step 3: Iterate through sorted strings and find the common prefix
        while i < len(s):
            j = 0
            while j < len(s[i-1]):
                if s[i-1][j] != s[i][j]:
                    break
                j += 1
            
            # Update the length of the common prefix
            length = min(length, j)
            
            if length == 0:
                break  # No common prefix found
            i += 1
        
        # Step 4: Return the common prefix
        return s[0][:length]
