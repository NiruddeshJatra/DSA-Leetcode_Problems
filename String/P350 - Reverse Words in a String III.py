# Time Complexity:
# - O(N) where N is the total length of string
# - split() takes O(N)
# - Reversing each word takes O(N) total
# - join() takes O(N)

# Space Complexity:
# - O(N) for storing words array
# - O(N) for storing final result string
# - Each word is stored once in memory

# INTUITION:
# Instead of character by character manipulation, we can:
# - Split string into words 
# - Reverse each word individually
# - Join words back together
# Example: "Let's take LeetCode contest"
# After split: ["Let's", "take", "LeetCode", "contest"]
# After reverse: ["s'teL", "ekat", "edoCteeL", "tsetnoc"]
# After join: "s'teL ekat edoCteeL tsetnoc"

# ALGO:
# 1. Split input string into array of words
# 2. For each word:
#    - Reverse characters in the word
# 3. Join reversed words with spaces
# 4. Return final reversed string

class Solution:
   def reverseWords(self, s: str) -> str:
       # Split string into words
       wordArray = s.split()
       
       # Reverse each word
       for i in range(len(wordArray)):
           wordArray[i] = wordArray[i][::-1]
           
       # Join words back together
       return ' '.join(wordArray)
