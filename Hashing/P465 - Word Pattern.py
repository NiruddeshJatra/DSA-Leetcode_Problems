# Time Complexity:
# - O(n + m), where n is the length of pattern and m is the length of string s
# - We split the string s into words: O(m)
# - We iterate through pattern and words once: O(n)
# - Hash map operations are O(1) on average

# Space Complexity:
# - O(n + w), where n is the number of unique characters in pattern and w is the number of unique words
# - We store two hash maps for bidirectional mapping
# - We also store the words array from splitting the string

# INTUITION:
# The problem requires checking if there's a bijective (one-to-one) mapping between pattern characters and words
# Key insights:
# - Each character in pattern must map to exactly one unique word
# - Each word must map to exactly one unique character
# - We need bidirectional mapping to ensure no conflicts
# Example:
# pattern = "abba", s = "dog cat cat dog"
# Mapping: a↔dog, b↔cat
# This works because each character maps to exactly one word and vice versa
# Counter-example: pattern = "abba", s = "dog cat cat fish"
# This fails because 'a' would map to both "dog" and "fish"

# ALGO:
# 1. Split the string into individual words
# 2. Check if pattern length matches number of words
# 3. Create two hash maps for bidirectional mapping:
#    - charToWord: maps pattern characters to words
#    - wordToChar: maps words to pattern characters
# 4. For each character-word pair:
#    - Check if character already maps to a different word
#    - Check if word already maps to a different character
#    - If conflicts exist, return False
# 5. If no conflicts found, return True

class Solution:
   def wordPattern(self, pattern: str, s: str) -> bool:
       # Create bidirectional mapping hash maps
       charToWord, wordToChar = {}, {}
       
       # Split string into individual words
       words = s.split(" ")
       
       # Check if lengths match
       if len(pattern) != len(words):
           return False
       
       # Check each character-word pair for valid mapping
       for patternChar, currentWord in zip(pattern, words):
           # Check character to word mapping
           if patternChar in charToWord and charToWord[patternChar] != currentWord:
               return False
           else:
               charToWord[patternChar] = currentWord
           
           # Check word to character mapping
           if currentWord in wordToChar and wordToChar[currentWord] != patternChar:
               return False
           else:
               wordToChar[currentWord] = patternChar
       
       # All mappings are consistent
       return True
