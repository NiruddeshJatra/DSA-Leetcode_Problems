from sys import *
from collections import *
from math import *
from typing import List

class Solution:
   def longestStrChain(self, words: List[str]) -> int:
       # Time Complexity:
       # - O(n² * L) where n is the number of words and L is the maximum length of any word
       # - Sorting takes O(n log n) time
       # - The nested loops take O(n²) iterations
       # - Each comparison between two words takes O(L) time
       
       # Space Complexity:
       # - O(n) for the dp array that stores the length of the longest chain ending with each word
       
       # INTUITION:
       # This problem is similar to the Longest Increasing Subsequence (LIS), but with a different condition.
       # Instead of comparing if one element is greater than another, we check if one word can form a predecessor
       # of another by removing exactly one character.
       #
       # For example, with words ["a", "b", "ba", "bca", "bda", "bdca"]:
       # - We first sort by length: ["a", "b", "ba", "bca", "bda", "bdca"]
       # - For "a", the longest chain is just itself: length 1
       # - For "b", the longest chain is just itself: length 1
       # - For "ba", we check if it can form a chain with "a" or "b" by removing one character
       #   "ba" -> remove "b" -> "a" (match found)
       #   So the longest chain ending at "ba" is 2 (["a", "ba"])
       # And so on...
       
       # ALGO:
       # 1. Define a helper function compare(word1, word2) that checks if word1 can be formed by adding one 
       #    character to word2 (making word2 a predecessor of word1)
       # 2. Sort the words by length to ensure we only compare words that could potentially form a chain
       # 3. Initialize a dp array where dp[i] represents the length of the longest chain ending with words[i]
       # 4. For each word at position i, check all previous words j:
       #    a. If words[i] can be formed by adding one character to words[j], update dp[i]
       # 5. Keep track of the maximum chain length found
       # 6. Return the maximum length
       
       # Helper function to check if word1 can be formed by adding one character to word2
       def compare(word1, word2):
           # If the length difference is not exactly 1, they can't form a valid chain
           if len(word1) != len(word2) + 1:
               return False
           
           # Use two pointers to compare characters
           i = j = 0
           
           # Iterate through both words
           while i < len(word1) and j < len(word2):
               # If characters match, move both pointers
               if word1[i] == word2[j]:
                   j += 1
               # If characters don't match, only move pointer for word1
               i += 1
           
           # If we've gone through all characters in word2, it's a predecessor
           return j == len(word2)
       
       # Sort words by length to ensure we only check valid predecessors
       words.sort(key=len)
       n = len(words)
       
       # dp[i] represents the length of the longest chain ending with words[i]
       dp = [1] * n  # Initialize with 1 as each word forms a chain of length 1 by itself
       
       # Variable to track the maximum chain length
       maxLength = 1
       
       # Fill the dp array
       for i in range(n):
           for j in range(i):
               # If words[j] is a predecessor of words[i] and using it leads to a longer chain
               if compare(words[i], words[j]) and dp[j] + 1 > dp[i]:
                   dp[i] = dp[j] + 1  # Update the length of the chain
           
           # Update the maximum length found so far
           maxLength = max(maxLength, dp[i])
       
       return maxLength
