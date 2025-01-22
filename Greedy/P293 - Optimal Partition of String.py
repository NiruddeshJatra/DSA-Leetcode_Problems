# Time Complexity:
# - O(N) where N is length of input string
# - We traverse the string once, doing O(1) set operations at each step

# Space Complexity:
# - O(K) where K is size of character set (at most 26 lowercase letters)
# - The set 'used' stores at most one instance of each unique character

# INTUITION:
# We can partition the string by tracking characters seen so far.
# When we encounter a character already in current partition,
# we need to start a new partition to ensure unique characters.
# This greedy approach gives minimum number of partitions needed.

# ALGO:
# 1. Initialize:
#    - Set to track characters in current partition
#    - Counter for number of partitions (start with 1)
# 2. Iterate through string:
#    - If current char exists in current partition:
#      * Clear set (start new partition)
#      * Increment partition counter
#    - Add current char to set
# 3. Return final partition count

class Solution:
   def partitionString(self, inputString: str) -> int:
       # Track characters in current partition
       currentPartitionChars = set()
       
       # Count of partitions needed (start with 1)
       partitionCount = 1
       
       # Process each character
       for char in inputString:
           # If char already in current partition
           if char in currentPartitionChars:
               # Start new partition
               currentPartitionChars.clear()
               partitionCount += 1
           
           # Add char to current partition
           currentPartitionChars.add(char)
       
       return partitionCount
