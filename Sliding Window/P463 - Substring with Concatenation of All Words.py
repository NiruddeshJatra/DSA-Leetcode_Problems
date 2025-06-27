# Time Complexity:
# - O(n * m), where n is the length of string s and m is the length of each word
# - We iterate through the string with wordLen different starting points
# - Each character is visited at most twice (once when expanding, once when contracting)

# Space Complexity:
# - O(k), where k is the number of unique words in the words array
# - We store word frequencies in hash maps

# INTUITION:
# The problem asks to find all starting indices where a concatenation of all words appears
# Key insights:
# - All words have the same length, so we can process the string in chunks
# - Use sliding window technique with multiple starting points
# - Track word frequencies to ensure exact matches
# Example:
# s = "barfoothefoobarman", words = ["foo","bar"]
# Valid concatenations: "foobar" at index 9, "barfoo" at index 0
# We need to check all possible arrangements of the given words

# ALGO:
# 1. Create frequency map of all words to match
# 2. For each possible starting offset (0 to wordLen-1):
#    - Use sliding window to track current words in the window
#    - Expand window by adding new words
#    - Contract window when word frequency exceeds requirement
#    - Record valid starting indices when window contains all words
# 3. Return all valid starting indices

class Solution:
   def findSubstring(self, s: str, words: List[str]) -> List[int]:
       # Create frequency map of target words
       targetWordFreq = Counter(words)
       result = []
       wordLength = len(words[0])
       totalWords = len(words)
       
       # Try all possible starting offsets (0 to wordLength-1)
       for startOffset in range(wordLength):
           windowStartIndex = startOffset
           currentWindowFreq = defaultdict(int)
           wordsInWindow = 0
           
           # Process string in chunks of wordLength
           for currentIndex in range(startOffset, len(s) - wordLength + 1, wordLength):
               currentWord = s[currentIndex:currentIndex + wordLength]
               
               # If current word is not in target words, reset window
               if currentWord not in targetWordFreq:
                   windowStartIndex = currentIndex + wordLength
                   currentWindowFreq = defaultdict(int)
                   wordsInWindow = 0
                   continue
               
               # Add current word to window
               currentWindowFreq[currentWord] += 1
               wordsInWindow += 1
               
               # Contract window if current word frequency exceeds target
               while currentWindowFreq[currentWord] > targetWordFreq[currentWord]:
                   leftWord = s[windowStartIndex:windowStartIndex + wordLength]
                   currentWindowFreq[leftWord] -= 1
                   wordsInWindow -= 1
                   windowStartIndex += wordLength
               
               # Check if we have a valid concatenation
               if wordsInWindow == totalWords:
                   result.append(windowStartIndex)
       
       return result
