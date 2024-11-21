# Time Complexity: O(n + m * log(m)), where `n` is the length of `nums` and `m` is the number of unique elements in `nums`.  
# - Building the frequency dictionary takes O(n).  
# - Sorting the dictionary by frequency takes O(m * log(m)), where `m` is the number of unique elements.  
# - Retrieving the top `k` keys takes O(k), which is negligible compared to sorting.  
# - Total complexity: O(n + m * log(m)).

# Space Complexity: O(n), where `n` is the length of `nums`.  
# - The frequency dictionary requires O(n) space in the worst case (if all elements are unique).  
# - Additional space is used for the sorted dictionary and list of keys, which are proportional to the number of unique elements.

# INTUITION:  
# The task is to find the `k` most frequent elements in the list `nums`.  
# To achieve this:  
# 1. Use a frequency dictionary to count the occurrences of each element in `nums`.  
# 2. Sort the elements by their frequencies in descending order.  
# 3. Select the top `k` elements from the sorted list.  
# This approach leverages the frequency dictionary to efficiently count elements and sorting to rank them by their frequency.

# ALGORITHM:  
# 1. Create a frequency dictionary (`freq`) to count occurrences of each element in `nums`.  
# 2. Sort the dictionary items by frequency in descending order.  
# 3. Extract the top `k` keys from the sorted list.  
# 4. Return the top `k` elements as the result.

from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a frequency dictionary
        freq = Counter(nums)

        # Sort the dictionary by frequency in descending order
        sortedFreq = dict(sorted(freq.items(), key=lambda x: -x[1]))

        # Extract the top k keys
        freqValues = list(sortedFreq.keys())

        # Return the top k most frequent elements
        return freqValues[:k]
