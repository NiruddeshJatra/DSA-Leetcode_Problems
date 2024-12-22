# Time Complexity: O(n), where n is the length of the array.
# - The loop iterates through the array once, and all operations (dictionary checks and updates) are O(1).
# - Hence, the overall complexity is linear.

# Space Complexity: O(n).
# - We use a dictionary `freq` to track the indices of elements, which in the worst case can store all the elements in the array.

# ALGORITHM:
# 1. Use a variable `start` to represent the index beyond which all elements are guaranteed to be processed.
# 2. Maintain a dictionary `freq` to track the last occurrence index of each element in `nums`.
# 3. Iterate through the array, and for each element:
#    - If the element is already in the dictionary `freq` and its last occurrence is greater than or equal to `start`:
#      - Perform the operation by incrementing `start` by 3 (removing the first 3 elements starting from `start`).
#      - Increment the operation count `count`.
#    - Update the last occurrence of the current element in `freq`.
# 4. Return the total count of operations.

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = start = 0  # Initialize the number of operations and the starting index.
        freq = {}          # Dictionary to track the last occurrence of each element.
        
        for i in range(len(nums)):
            # If the current element was already seen after the `start` index, perform the operation.
            while nums[i] in freq and freq[nums[i]] >= start:
                start += 3  # Remove 3 elements starting from `start`.
                count += 1  # Increment the operation count.
            
            # Update the last occurrence index of the current element.
            freq[nums[i]] = i
        
        return count

# Example Usage:
# Input: nums = [1, 2, 2, 3, 1]
# Output: 1 (One operation is enough to make all elements distinct)
solution = Solution()
print(solution.minimumOperations([1, 2, 2, 3, 1]))  # Output: 1
