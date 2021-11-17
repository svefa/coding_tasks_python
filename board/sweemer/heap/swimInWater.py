# 788. You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

def swimInWater(grid):
    N =len(grid)

    seen = {(0,0)}
    pq = [(grid[0][0], 0, 0)]
    ans = 0
    while pq:
        d,r,c = heapq.heappop(pq)
        ans = max(ans,d)
        if r==c==N-1: return ans
        for i,j in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
            if 0 <=i < N and 0 <= j < N and (i,j) not in seen:
                heapq.heappush(pq, (grid[i][j], i,j))
                seen.add(i,j)


