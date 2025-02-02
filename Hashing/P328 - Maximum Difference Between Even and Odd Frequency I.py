# Time Complexity:
# - O(N) for creating frequency counter
# - O(K) for filtering frequencies, where K is unique characters
# - O(K) for finding min/max
# - Overall O(N) where N is length of string

# Space Complexity:
# - O(K) for frequency counter, where K is unique characters
# - O(K) for filtered even/odd frequency lists
# - Overall O(K) where K <= 26 for lowercase letters

# INTUITION:
# For each character frequency:
# - Even frequencies must stay even after moving chars
# - Odd frequencies must stay odd after moving chars
# We want maximum difference between:
# 1. Max odd - Min even
# 2. Min odd - Max even
# Example: s = "abccba"
# Frequencies: a:2, b:2, c:2 (all even)
# No odd frequencies, so return 0
# Example: s = "abcccba"
# Frequencies: a:2, b:2, c:3
# Even: [2,2], Odd: [3]
# Max possible: 3-2 = 1

# ALGO:
# 1. Count frequency of each character
# 2. Split frequencies into even and odd lists
# 3. If either list empty, return 0
#    (can't make valid difference)
# 4. Return max of:
#    - Largest odd - Smallest even
#    - Smallest odd - Largest even

def maxDifference(self, s: str) -> int:
   # Count frequency of each character
   charFrequencies = Counter(s)
   
   # Split frequencies into even and odd lists
   evenFrequencies = [freq for freq in charFrequencies.values() 
                     if freq % 2 == 0]
   oddFrequencies = [freq for freq in charFrequencies.values() 
                    if freq % 2 == 1]
   
   # If either list is empty, no valid difference possible
   if not evenFrequencies or not oddFrequencies:
       return 0
   
   # Return maximum possible difference
   return max(
       max(oddFrequencies) - min(evenFrequencies),
       min(oddFrequencies) - max(evenFrequencies)
   )
