# Time Complexity: O(n*log(n)), where n is the length of the input list 'arr'.
#                   Sorting the set of unique elements takes O(n*log(n)) time.
# Space Complexity: O(n), where n is the number of unique elements in 'arr'.

# INTUITION:
# The code aims to assign ranks to each element in the input list 'arr', such that 
# the rank is based on the element's position in the sorted order of unique elements 
# in 'arr'. It uses a dictionary ('rankDict') to store the rank of each unique element 
# and a list ('rankArr') to store the ranks of corresponding elements in 'arr'.

# ALGO:
# 1. Create a sorted set ('sortedArr') of unique elements in 'arr' to obtain a sorted 
#    order of elements without duplicates.
# 2. Create a dictionary ('rankDict') to store the rank of each element in 'sortedArr'.
#    - Enumerate through 'sortedArr' and assign ranks starting from 1.
#    - Store the rank of each element in 'rankDict' with the element as the key.
# 3. Iterate through each element 'i' in 'arr':
#    - Append the rank of 'i' from 'rankDict' to 'rankArr'.
# 4. Return 'rankArr' as the result, which contains the ranks of elements in 'arr'.

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sortedArr = sorted(set(arr))  # Get unique elements in sorted order.
        rankDict = {}  # Dictionary to store ranks.
        
        # Assign ranks to each unique element.
        for rank, value in enumerate(sortedArr):
            rankDict[value] = rank + 1
        
        rankArr = []  # List to store ranks of elements in 'arr'.
        
        # Get ranks of corresponding elements in 'arr'.
        for i in arr:
            rankArr.append(rankDict[i])
        
        return rankArr  # Return the list of ranks.
