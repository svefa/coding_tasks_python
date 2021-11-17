def swimInWater(grid):
    N=len(grid)
    def possible(T):
        stack = [(0,0)]
        seen = {(0,0)}
        while stack:
            r,c =stack.pop()
            if r==c==N-1: return True
            for i,j in ((r-1,c), (r,c-1), (r+1,c), (r, c+1)):
                if 0 <= i < N and 0 <= j < N and (i,j) not in seen and grid[i][j] <= T:
                    stack.append((i,j))
                    seen.add((i,j))
        return False
    
    lo, hi = grid[0][0], N*N
    while lo < hi:
        mi = (lo + hi)//2
        if not possible(mi):
            lo = mi + 1
        else:
            hi = mi
    return lo
