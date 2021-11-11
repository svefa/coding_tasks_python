from typing import List
class Solution:
    def bt(self, queens, n):
        j = len(queens)
        if j == n: 
            return 1
        s = 0
        for i in range(n):
            b = True #candidate
            # check i,j
            for k in range(j):
                # queen k,m
                m = queens[k]
                if m==i or k-m == j-i or k+m == j+i: 
                    b = False
                    break
            if b: s+= self.bt(queens+[i], n) 
        return s
    def totalNQueens(self, n: int) -> int:
        return self.bt([], n)


print("!",Solution().totalNQueens(4))        