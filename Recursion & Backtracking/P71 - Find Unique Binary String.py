# APPROACH 1

# Time Complexity: O(2^n)
# Space Complexity: O(2^n)

# INTUITION:
# The goal is to find a binary string of length `n` that is not present in the given list `nums` of binary strings. To achieve this, we can generate all possible binary strings of length `n` using backtracking. We start with an empty string and recursively add '0' and '1' to generate all possible permutations. Once all permutations are generated, we check which one is not present in `nums` and return it.

# ALGO:
# 1. Initialize an empty list `temp` to keep track of the current binary string and an empty list `ans` to store all binary permutations.
# 2. Define a recursive function `binaryPermutations` to generate all binary strings of length `n`:
#     2.1 If the length of `temp` is equal to the length of `nums`, join `temp` into a string and append it to `ans`, then return.
#     2.2 Append '0' to `temp`, call `binaryPermutations` recursively, and then remove the last character from `temp`.
#     2.3 Append '1' to `temp`, call `binaryPermutations` recursively, and then remove the last character from `temp`.
# 3. Call the `binaryPermutations` function to generate all binary permutations.
# 4. Iterate over each string in `ans` and check if it is not in `nums`. If found, return that string.
# 5. If no unique string is found, return -1.

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        temp, ans = [], []

        def binaryPermutations():
            if len(temp) == len(nums):
                ans.append("".join(temp))
                return
            temp.append("0")
            binaryPermutations()
            temp.pop()
            temp.append("1")
            binaryPermutations()
            temp.pop()

        binaryPermutations()
        for i in ans:
            if i not in nums:
                return i

        return -1

# APPROACH 2

# Time Complexity: O(n)
        # Space Complexity: O(n)
        
        # INTUITION:
        # The problem can be efficiently solved using Cantor's diagonalization argument. 
        # The idea is to construct a binary string that is guaranteed to be different from 
        # all given binary strings by ensuring that it differs in at least one bit position 
        # from each given string.
        
        # ALGO:
        # 1. Initialize an empty list `res` to store the resulting binary string.
        # 2. Iterate through each position `i` from 0 to n-1.
        #     2.1 Check the `i`-th bit of the `i`-th string in the input list `nums`.
        #     2.2 If the bit is '0', append '1' to `res`.
        #     2.3 Otherwise, append '0' to `res`.
        # 3. Join the list `res` into a string and return it.
        
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        res = []
        for i in range(n):
            if nums[i][i] == '0':
                res.append('1')
            else:
                res.append('0')
        return "".join(res)
