# Time Complexity:
# - O(k * log(min(k, m))), where m is the length of nums1 and k is the number of pairs we need to find.
# - We perform up to k heap operations, each taking O(log(size of heap)) time.
# - The heap size is bounded by min(k, length of nums1).

# Space Complexity:
# - O(min(k, m)) for the heap, where m is the length of nums1.
# - O(k) for the result list that stores the k pairs.

# INTUITION:
# This problem asks us to find the k pairs with the smallest sums from two sorted arrays.
# The key insight is to use a min-heap to track potential pairs in order of their sums.
#
# Initially, we add all pairs of the form (nums1[i], nums2[0]) to the heap, as these are potential candidates
# for smallest sums since nums2[0] is the smallest element in nums2.
#
# Then, for each pair we extract from the heap, we add the next pair (nums1[i], nums2[j+1]) to the heap.
# This approach ensures we explore pairs in order of increasing sum.
#
# For example, with nums1=[1,7,11], nums2=[2,4,6], k=3:
# 1. Initial heap: [(1+2,0), (7+2,0), (11+2,0)] = [(3,0), (9,0), (13,0)]
# 2. Pop (3,0): Add [1,2] to result and push (1+4,1) = (5,1) to heap
# 3. Pop (5,1): Add [1,4] to result and push (1+6,2) = (7,2) to heap
# 4. Pop (7,2): Add [1,6] to result and k=0, so we're done
# Result: [[1,2], [1,4], [1,6]]

# ALGO:
# 1. Initialize an empty result list and a min-heap.
# 2. Add all pairs of the form (nums1[i] + nums2[0], 0) to the heap, where the first element is the sum
#    and the second element is the index in nums2.
# 3. While k > 0 and the heap is not empty:
#    a. Pop the smallest pair (sum, index) from the heap.
#    b. Calculate the original elements from nums1 and nums2 that formed this pair.
#    c. Add those elements as a pair to the result list.
#    d. If there are more elements in nums2 (index + 1 < len(nums2)), add the next pair
#       (nums1[i] + nums2[index+1], index+1) to the heap.
#    e. Decrement k.
# 4. Return the result list containing the k pairs with the smallest sums.

from typing import List
import heapq

class Solution:
   def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
       # Handle edge cases
       if not nums1 or not nums2:
           return []
       
       # Initialize result list and min-heap
       smallestPairs = []
       minHeap = []
       
       # Add initial pairs to the heap
       # We only need to consider the first element from nums2 initially
       for num1 in nums1:
           # Store the sum and the index in nums2, along with the value from nums1
           heapq.heappush(minHeap, [num1 + nums2[0], 0, num1])
       
       # Extract k smallest pairs
       while k > 0 and minHeap:
           # Extract the smallest sum pair from the heap
           currentSum, index2, num1 = heapq.heappop(minHeap)
           num2 = nums2[index2]
           
           # Add the pair to the result
           smallestPairs.append([num1, num2])
           
           # Add the next pair with the same num1 but next element from nums2
           if index2 + 1 < len(nums2):
               nextNum2 = nums2[index2 + 1]
               heapq.heappush(minHeap, [num1 + nextNum2, index2 + 1, num1])
           
           # Decrement k
           k -= 1
       
       return smallestPairs
