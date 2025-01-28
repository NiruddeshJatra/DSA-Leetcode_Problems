# Time Complexity:
# - O(N), where N is the length of dominoes string
# - Single pass through the string with constant time operations

# Space Complexity:
# - O(N) to store the result string
# - Original string is not modified

# INTUITION:
# Process each segment between non-dot characters. The state of middle dominoes
# depends on forces from both sides. Add boundaries 'L' and 'R' to handle edges.
# For each segment, fill middle based on forces:
# - Same force: Fill all with that force
# - L...R: No force affects middle dots
# - R...L: Forces meet in middle, split equally

# ALGO:
# 1. Add boundary 'L' and 'R' to string
# 2. Use two pointers i,j to find segments between forces
# 3. Process each segment based on forces:
#    - Same force: Fill all with that force
#    - L...R: Fill with dots
#    - R...L: Fill half R, half L, middle dot if odd length
# 4. Build result string progressively

class Solution:
   def pushDominoes(self, dominoes: str) -> str:
       resultString = ''
       paddedDominoes = 'L' + dominoes + 'R'
       leftPtr = 0
       
       for rightPtr in range(1, len(paddedDominoes)):
           if paddedDominoes[rightPtr] == '.':
               continue
           
           middleLength = rightPtr - leftPtr - 1
           
           if leftPtr > 0:
               resultString += paddedDominoes[leftPtr]
               
           if paddedDominoes[leftPtr] == paddedDominoes[rightPtr]:
               resultString += paddedDominoes[leftPtr] * middleLength
           elif paddedDominoes[leftPtr] == 'L' and paddedDominoes[rightPtr] == 'R':
               resultString += '.' * middleLength
           else:  # R...L case
               resultString += 'R' * (middleLength // 2) + '.' * (middleLength % 2) + 'L' * (middleLength // 2)
               
           leftPtr = rightPtr
           
       return resultString
