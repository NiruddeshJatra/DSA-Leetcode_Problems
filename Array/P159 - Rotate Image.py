class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        # transpose
        for i in range(len(mat)):
            for j in range(i,len(mat)):
                mat[i][j],mat[j][i] = mat[j][i],mat[i][j]

        # reverse
        for i in range(len(mat)):
            for j in range(len(mat)//2):
        	    mat[i][j],mat[i][len(mat)-1-j] = mat[i][len(mat)-1-j],mat[i][j]
