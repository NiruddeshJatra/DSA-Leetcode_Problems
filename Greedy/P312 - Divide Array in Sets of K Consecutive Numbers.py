# Time Complexity:
# - O(N log N + N*K), where N is length of nums and K is group size
# - Sorting unique numbers is O(M log M) where M is number of unique values
# - For each number, we check K consecutive numbers

# Space Complexity:
# - O(M) where M is number of unique values in nums
# - Counter dictionary stores frequency of each unique number

# INTUITION:
# Count frequency of each number and try to form groups starting from smallest
# number. Each group must have K consecutive integers. If at any point we can't 
# complete a group of K consecutive numbers, return False.

# ALGO:
# 1. Check if array length is divisible by K
# 2. Create frequency counter for nums
# 3. Sort unique numbers to process in order
# 4. For each number:
#    - While its frequency > 0:
#      - Try to form group of K consecutive nums
#      - Reduce frequency of each used number
#      - If any required number missing, return False
# 5. Return True if all groups formed successfully

class Solution:
   def isPossibleDivide(self, nums: List[int], k: int) -> bool:
       if len(nums) % k != 0:
           return False
           
       numberFreq = Counter(nums)
       
       for currentNum in sorted(numberFreq):
           while numberFreq[currentNum] > 0:
               for consecutiveNum in range(currentNum, currentNum + k):
                   numberFreq[consecutiveNum] -= 1
                   if numberFreq[consecutiveNum] < 0:
                       return False
                       
       return True
