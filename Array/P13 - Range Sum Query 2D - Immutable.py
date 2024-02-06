# Time Complexity: O(m*n) for initialization, where m is the number of rows and n is the number of columns in the matrix.
#                  O(1) for each sumRegion query.
# Space Complexity: O(m*n) for storing the precomputed sums.

# INTUITION:
# The code initializes a NumMatrix object with a given matrix. During initialization, 
# it precomputes the sum of all submatrices using the prefix sum technique and stores 
# them in the 'preSum' matrix. The 'sumRegion' method then uses these precomputed sums 
# to efficiently calculate the sum of a specified region in constant time.

# ALGO:
# 1. Initialize the NumMatrix object with the input matrix.
# 2. Calculate and store the cumulative sums of all submatrices in the 'preSum' matrix 
#    using the prefix sum technique.
# 3. Implement the 'sumRegion' method to return the sum of the specified region using 
#    the precomputed sums from 'preSum'.

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

        self.m,self.n = len(matrix), len(matrix[0])
        
        self.preSum = [[0 for j in range(self.n+1)] for i in range(self.m+1)]
        
        for i in range(1,self.m+1):
            for j in range(1,self.n+1):
                self.preSum[i][j] = self.preSum[i][j-1] + self.preSum[i-1][j] -self.preSum[i-1][j-1] + matrix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.preSum[row2+1][col2+1] - self.preSum[row1][col2+1] - self.preSum[row2+1][col1] + self.preSum[row1][col1]
                
        return ans
