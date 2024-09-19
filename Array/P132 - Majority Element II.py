# Time Complexity: O(n), where n is the number of elements in the `nums` list.
# The algorithm makes two passes through the list: one for identifying potential candidates, and another for verifying them. Both passes are linear.
# Space Complexity: O(1), as we are using only a few extra variables (count1, count2, candidate1, candidate2), regardless of the input size.

# INTUITION:
# This solution is based on the Boyer-Moore Voting Algorithm, which efficiently finds elements that appear more than ⌊n/3⌋ times.
# The problem asks us to find all elements that appear more than ⌊n/3⌋ times in the array. Since there can be at most two such elements, we use two candidates and their corresponding counts.

# ALGO:
# 1. Use two variables to store potential majority elements (`candidate1` and `candidate2`), and their corresponding counts (`count1` and `count2`).
# 2. In the first pass through the list, for each number:
#    - If `count1` is 0 and the current number is not equal to `candidate2`, set `candidate1` to the current number and reset `count1` to 1.
#    - If `count2` is 0 and the current number is not equal to `candidate1`, set `candidate2` to the current number and reset `count2` to 1.
#    - If the current number is equal to `candidate1`, increment `count1`.
#    - If the current number is equal to `candidate2`, increment `count2`.
#    - If the current number is not equal to either candidate, decrement both counts.
# 3. In the second pass, count the occurrences of `candidate1` and `candidate2`.
# 4. Return the candidates that appear more than ⌊n/3⌋ times.

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Step 1: Initialize counts and candidates
        count1, count2 = 0, 0
        candidate1, candidate2 = 0, 0
        
        # Step 2: First pass to find potential candidates
        for num in nums:
            if count1 == 0 and num != candidate2:
                count1 = 1
                candidate1 = num
            elif count2 == 0 and num != candidate1:
                count2 = 1
                candidate2 = num
            elif num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        # Step 3: Second pass to count actual occurrences
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
        
        # Step 4: Check if candidates appear more than ⌊n/3⌋ times
        res = []
        if count1 > len(nums) // 3:
            res.append(candidate1)
        if count2 > len(nums) // 3:
            res.append(candidate2)
        
        return res
