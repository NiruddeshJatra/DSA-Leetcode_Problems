# Time Complexity:
# - O(N) where N is total number of characters across all words
# - Single pass through words with constant-time operations

# Space Complexity:
# - O(N) to store justified text result
# - Temporary storage for current line processing

# INTUITION:
# Text justification requires careful space distribution:
# - Distribute spaces evenly between words
# - Extra spaces added from left to right
# - Last line left-justified with spaces at end
# - Single word lines fully padded with spaces

# ALGO:
# 1. Track current line's words, length
# 2. When line exceeds max width:
#    - Handle single word lines differently
#    - Distribute spaces evenly for multiple words
#    - Handle extra spaces distribution
# 3. Final line left-justified with trailing spaces

class Solution:
   def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
       result = []
       currentLineWords = []
       currentLineLength = 0
       
       for word in words:
           # Check if adding word exceeds max width
           if currentLineLength + len(word) + len(currentLineWords) > maxWidth:
               # Process current line
               if len(currentLineWords) == 1:
                   # Single word line
                   line = currentLineWords[0] + ' ' * (maxWidth - currentLineLength)
               else:
                   # Multiple word line
                   totalSpaces = maxWidth - currentLineLength
                   spaceBetweenWords = totalSpaces // (len(currentLineWords) - 1)
                   extraSpaces = totalSpaces % (len(currentLineWords) - 1)
                   
                   line = ''
                   for i, lineWord in enumerate(currentLineWords[:-1]):
                       line += lineWord
                       line += ' ' * (spaceBetweenWords + (1 if i < extraSpaces else 0))
                   line += currentLineWords[-1]
               
               result.append(line)
               
               # Reset for next line
               currentLineWords = []
               currentLineLength = 0
           
           # Add current word to line
           currentLineWords.append(word)
           currentLineLength += len(word)
       
       # Handle last line
       if currentLineWords:
           lastLine = ' '.join(currentLineWords)
           lastLine += ' ' * (maxWidth - len(lastLine))
           result.append(lastLine)
       
       return result
