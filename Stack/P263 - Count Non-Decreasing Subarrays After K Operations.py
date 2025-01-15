# Time Complexity:
# - O(N) where N is length of array
# - Each element enters and exits queue at most once

# Space Complexity:
# - O(N) for the deque in worst case

# INTUITION:
# The problem involves finding count of subarrays where sum of replacing elements with larger ones
# doesn't exceed k. We use a "replacement cost" approach where:
# 1. When we find a larger element, we calculate cost of replacing smaller elements before it
# 2. Use sliding window to maintain valid subarrays within budget k
# 3. Monotonic queue helps track which elements need replacement

# ALGORITHM:
# 1. Reverse array to handle replacements more efficiently
# 2. Use deque to maintain monotonic increasing sequence
# 3. For each element:
#    - Update replacement costs when finding larger elements
#    - Shrink window from left when over budget
#    - Count valid subarrays ending at current element

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        # Reverse array to process replacements from right to left
        nums = nums[::-1]
        totalCount = 0
        queue = deque()
        leftIndex = 0
        
        for rightIndex in range(len(nums)):
            # Update replacement costs for larger elements
            while queue and nums[queue[-1]] < nums[rightIndex]:
                replacedIndex = queue.pop()
                previousIndex = queue[-1] if queue else (leftIndex - 1)
                
                # Calculate cost of replacements
                elementsToReplace = replacedIndex - previousIndex
                increaseCost = nums[rightIndex] - nums[replacedIndex]
                k -= elementsToReplace * increaseCost
            
            queue.append(rightIndex)
            
            # Shrink window if over budget
            while k < 0:
                # Remove index from queue if it's leaving window
                if queue[0] == leftIndex:
                    queue.popleft()
                else:
                    # Add back cost of removing leftmost element
                    k += nums[queue[0]] - nums[leftIndex]
                
                leftIndex += 1
            
            # Count valid subarrays ending at current position
            totalCount += rightIndex - leftIndex + 1
            
        return totalCount
