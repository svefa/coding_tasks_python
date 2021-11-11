from typing import List
class Solution:
    def divideAndConquer(self, matrix, i1,j1, i2,j2, target) ->bool:
        if i1>i2 or j1>j2: return False
        print(i1,j1, i2,j2, target)
        if target < matrix[i1][j1] or matrix[i2][j2] < target : return False
        if target == matrix[i1][j1] or matrix[i2][j2] == target : return True

        if i1==i2 and j1==j2: return target == matrix[i1][j1]
        i, j = (i1+i2)//2, (j1+j2)//2
        if target == matrix[i][j]: return True
        if self.divideAndConquer( matrix, i1,j1, i,j, target): return True
        if self.divideAndConquer( matrix, i+1,j+1, i2,j2, target): return True
        if self.divideAndConquer( matrix, i+1,j1, i2,j, target): return True
        if self.divideAndConquer( matrix, i1,j+1, i,j2, target): return True
        return False
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.divideAndConquer(matrix, 0,0, len(matrix)-1, len(matrix[0])-1, target)


#matrix=[[1,4,7,11,15],
#        [2,5,8,12,19],
#        [3,6,9,16,22],
#        [10,13,14,17,24],
#        [18,21,23,26,30]]
#target=5 
#res = Solution().searchMatrix(matrix,target)
#print(res)

matrix=[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target=20
res = Solution().searchMatrix(matrix,target)
print(res)