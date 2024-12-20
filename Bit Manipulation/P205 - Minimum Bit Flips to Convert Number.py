class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = start ^ goal
        count = 0
        while ans:
            count += 1
            ans &= ans-1

        return count
