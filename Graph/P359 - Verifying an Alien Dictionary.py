# Time Complexity:
# - O(M) to build character order mapping, where M is length of order string
# - O(N * K) to compare words, where:
#   N = number of adjacent word pairs to compare
#   K = length of shorter word in each comparison
# - Overall: O(M + N*K)

# Space Complexity: 
# - O(1) for character order mapping (26 letters max)
# - No other significant space used
# - Overall: O(1) since alphabet size is fixed

# INTUITION:
# Imagine you're checking if words in a foreign dictionary are properly sorted.
# In English, we know a comes before b, which comes before c, and so on.
# But in this alien language, the letters might follow a different order!
#
# For example, if in alien language:
# - 'h' comes before 'l'
# - 'l' comes before 'a'
# Then "hello" must come before "lamp"
#
# We can solve this by:
# 1. First learning the alien alphabet order (like memorizing their ABC's)
# 2. Then checking if pairs of words follow this order
# 3. Also handling the special case where one word is prefix of another
#    (like "app" vs "apple" - shorter word must come first)

# ALGORITHM:
# 1. Create mapping of alien characters to their positions (like a=0, b=1 in English)
# 2. Compare adjacent words pairwise:
#    - If word1 is longer and word2 is its prefix, order is invalid
#    - Compare characters until we find different ones
#    - First different characters determine if order is valid
# 3. If all comparisons pass, order is valid

class Solution:
   def isAlienSorted(self, words: List[str], order: str) -> bool:
       # Create mapping of alien character -> position (like a=0, b=1 in English)
       alienOrder = {}
       for position, character in enumerate(order):
           alienOrder[character] = position
           
       # Check each adjacent pair of words
       for wordIndex in range(len(words) - 1):
           currentWord = words[wordIndex]
           nextWord = words[wordIndex + 1]
           
           # Handle case where longer word is prefix of shorter word
           # Example: "apple" should not come before "app"
           if len(currentWord) > len(nextWord) and currentWord[:len(nextWord)] == nextWord:
               return False
               
           # Compare characters until we find a difference
           for char1, char2 in zip(currentWord, nextWord):
               # If first character is smaller, order is good for this pair
               if alienOrder[char1] < alienOrder[char2]:
                   break
               # If first character is larger, order is invalid
               if alienOrder[char1] > alienOrder[char2]:
                   return False
                   
       # All pairs are in correct order
       return True
