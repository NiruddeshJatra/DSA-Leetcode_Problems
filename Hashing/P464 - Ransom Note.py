# Time Complexity:
# - O(n + m), where n is the length of ransomNote and m is the length of magazine
# - We iterate through the magazine once to build the frequency map: O(m)
# - We iterate through the ransomNote once to check availability: O(n)

# Space Complexity:
# - O(k), where k is the number of unique characters in the magazine
# - We store character frequencies in a hash map

# INTUITION:
# The problem asks if we can construct a ransom note using letters from a magazine
# Key constraints:
# - Each letter in the magazine can only be used once
# - We need to check if magazine has enough of each required letter
# Strategy:
# - Count frequency of all letters available in the magazine
# - For each letter needed in ransom note, check availability and consume it
# Example:
# ransomNote = "aab", magazine = "baa"
# Magazine has: a=2, b=1
# Need: a=2, b=1
# This works because we have exactly what we need

# ALGO:
# 1. Create frequency counter for all characters in magazine
# 2. For each character in ransom note:
#    - Check if character exists in magazine with count > 0
#    - If not available, return False
#    - If available, decrement the count (consume the letter)
# 3. If all characters are successfully consumed, return True

class Solution:
   def canConstruct(self, ransomNote: str, magazine: str) -> bool:
       # Count frequency of each character in the magazine
       magazineCharFreq = Counter(magazine)
       
       # Check each character in the ransom note
       for requiredChar in ransomNote:
           # If character not available or already exhausted
           if requiredChar not in magazineCharFreq or magazineCharFreq[requiredChar] == 0:
               return False
           
           # Consume one instance of this character from magazine
           magazineCharFreq[requiredChar] -= 1
       
       # All required characters were successfully found and consumed
       return True
