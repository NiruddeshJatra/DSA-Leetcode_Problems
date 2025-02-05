# Time Complexity:
# - O(N) where N is the length of the input array
# - Each character is processed exactly once
# - Converting counts to string takes constant time as numbers are bounded

# Space Complexity:
# - O(1) as we modify the array in-place
# - Only use a few variables regardless of input size
# - The compressed string overwrites the original array

# INTUITION:
# We can compress the string in-place by:
# - Keeping track of the current position we're reading from
# - Keeping track of where we're writing the compressed result
# - When we find repeated characters, we count them and write the count
# Example: For "aabbcc" -> "a2b2c2"
# At each step:
# 1. See 'a', count=2, write: "a2...."
# 2. See 'b', count=2, write: "a2b2.."
# 3. See 'c', count=2, write: "a2b2c2"

# ALGO:
# 1. Use two pointers: one for reading (currentIndex) and one for writing (compressedIndex)
# 2. For each character:
#    - Count consecutive occurrences
#    - Write the character
#    - If count > 1, write the count digits
# 3. Return the length of compressed string

class Solution:
   def compress(self, chars: List[str]) -> int:
       writeIndex = readIndex = 0
       
       while readIndex < len(chars):
           currentChar = chars[readIndex]
           charCount = 0
           
           # Count consecutive occurrences of currentChar
           while readIndex < len(chars) and chars[readIndex] == currentChar:
               charCount += 1
               readIndex += 1
           
           # Write character
           chars[writeIndex] = currentChar
           writeIndex += 1
           
           # Write count if greater than 1
           if charCount > 1:
               for digit in str(charCount):
                   chars[writeIndex] = digit
                   writeIndex += 1
       
       return writeIndex
