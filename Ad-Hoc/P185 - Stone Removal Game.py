class Solution:
    def canAliceWin(self, n: int) -> bool:
        if 10 <= n <= 18 or 27 <= n <= 33 or 40 <= n <= 44 or 49 <= n <= 50:
            return True
        return False
