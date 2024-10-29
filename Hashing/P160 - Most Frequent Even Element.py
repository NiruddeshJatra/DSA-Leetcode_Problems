# Time Complexity: O(n), where n is the number of elements in the `nums` list.
# We traverse the list once to populate the hashmap and once more to determine the most frequent even number.

# Space Complexity: O(n), because we use a hashmap to store the frequency of even numbers in `nums`.

# INTUITION:
# The problem requires finding the most frequent even number in a list. 
# If multiple even numbers have the same highest frequency, we should return the smallest among them.

# ALGO:
# 1. Traverse through the list, and for each even number, update its frequency count in a hashmap.
# 2. Traverse the hashmap to identify the even number with the highest frequency.
# 3. If multiple even numbers have the same frequency, choose the smallest one.
# 4. If no even numbers are found, return -1.

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        # Step 1: Build frequency hashmap for even numbers
        hashmap = {}
        for num in nums:
            if num % 2 == 0:
                hashmap[num] = hashmap.get(num, 0) + 1

        # Step 2: Determine the most frequent even number
        ans, maxFreq = float('inf'), 0
        for num, cnt in hashmap.items():
            if cnt > maxFreq or (cnt == maxFreq and num < ans):
                maxFreq = cnt
                ans = num

        # Step 3: Return result or -1 if no even number found
        return ans if maxFreq else -1
