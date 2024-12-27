# Time Complexity:
# - addNum: O(log N), where N is total numbers
#   - Each heap operation (push/pop) takes O(log N)
#   - We do at most 2 heap operations per addition
# - findMedian: O(1)
#   - Just accessing top elements of heaps
#   - No heap operations needed

# Space Complexity:
# - O(N) where N is total numbers stored
#   - Two heaps each storing roughly N/2 elements
#   - small heap stores lower half of numbers
#   - large heap stores upper half of numbers

# INTUITION:
# To find running median efficiently, we can:
# - Split numbers into two halves (small and large)
# - Use max heap for small half and min heap for large half
# - Keep heaps balanced (diff in size ≤ 1)
# - Tops of heaps give us middle elements
# This way median can be found in O(1) time after each addition

# ALGO:
# 1. Maintain two heaps:
#    - small (max heap): stores lower half of numbers
#    - large (min heap): stores upper half of numbers
# 2. When adding number:
#    - If heaps equal size:
#      * Add to small, take max and add to large
#    - If large is bigger:
#      * Add to large, take min and add to small
# 3. For finding median:
#    - If equal size: average of tops
#    - If unequal: top of large heap

class MedianFinder:
   def __init__(self):
       # Initialize heaps
       self.small = []  # max heap for smaller half
       self.large = []  # min heap for larger half
       
   def addNum(self, num: int) -> None:
       if len(self.small) == len(self.large):
           # Add to small, move largest to large
           heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
       else:
           # Add to large, move smallest to small
           heapq.heappush(self.small, -heapq.heappushpop(self.large, num))
           
   def findMedian(self) -> float:
       if len(self.small) == len(self.large):
           # Average of middle two numbers
           return float(self.large[0] - self.small[0]) / 2.0
       else:
           # Middle number from large heap
           return float(self.large[0])
