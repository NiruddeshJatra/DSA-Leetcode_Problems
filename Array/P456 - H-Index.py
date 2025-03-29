# Time Complexity:
# - O(n log n), where n is the number of papers
# - Sorting the citations array takes O(n log n)
# - The subsequent loop takes O(n) time

# Space Complexity:
# - O(1) since we only use a constant amount of extra space
# - The sorting is typically done in-place

# INTUITION:
# The h-index measures both the quantity and impact of a researcher's publications
# Definition: h-index is the maximum value h where the researcher has at least h papers with at least h citations each
# Key insight:
# - After sorting citations, we can efficiently find the largest h-index
# - We check each position to see if the citation count at that position is large enough
# Example:
# citations = [0,1,3,5,6]
# When sorted, we check:
# - citations[0] = 0 ≥ 5-0? No
# - citations[1] = 1 ≥ 5-1? No
# - citations[2] = 3 ≥ 5-2? No
# - citations[3] = 5 ≥ 5-3? Yes, so h-index = 5-3 = 2
# This means the researcher has 2 papers with at least 2 citations each

# ALGO:
# 1. Sort the citations array in ascending order
# 2. Iterate through the sorted array
# 3. For each position, check if the number of citations at that position
#    is greater than or equal to the number of papers remaining
# 4. Return the maximum such value found
# 5. If no valid h-index is found, return 0

class Solution:
   def hIndex(self, citations: List[int]) -> int:
       # Sort the citations array in ascending order
       citations.sort()
       
       # Get the number of papers
       paperCount = len(citations)
       
       # Iterate through the sorted citations
       for currentPaper in range(paperCount):
           # Calculate remaining papers (including current)
           remainingPapers = paperCount - currentPaper
           
           # Check if we found a valid h-index
           # The current paper and all papers after it have at least 
           # 'remainingPapers' citations
           if citations[currentPaper] >= remainingPapers:
               return remainingPapers
       
       # If no valid h-index is found, return 0
       return 0
