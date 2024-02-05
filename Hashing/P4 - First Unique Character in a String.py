# Time Complexity: O(n), where n is the length of the input string 's'.
# Space Complexity: O(1) or O(m), where m is the number of unique characters in 's'.

# INTUITION:
# The code counts the frequency of each character in the string using a Counter object, 
# then iterates through the string again to find the first non-repeating character by 
# checking the frequency of each character. It returns the index of the first non-repeating 
# character found. 

# ALGO:
# 1. Initialize a Counter object to count the frequency of characters in the string.
# 2. Iterate through the items (character-frequency pairs) in the Counter object.
#    2.1. If the frequency of the character is 1, assign it to 'singleChar' and break the loop.
# 3. Iterate through the characters in the string using enumerate.
#    3.1. If the current character matches 'singleChar', return its index.
# 4. If no non-repeating character is found, return -1.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)
        singleChar = ""
        for i, j in freq.items():
            if j == 1:
                singleChar = i
                break
        for i, char in enumerate(s):
            if char == singleChar:
                return i
        return -1
