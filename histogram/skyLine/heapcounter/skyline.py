class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        res = [[0,0]]
        temp = []
        cnt = {0:1}
        heights = [0]
        for i,j,h in (buildings):
            #=buildings
            temp.append((i,-h))
            temp.append((j, h))
            cnt[abs(h)] = 0
        temp.sort()
        for i,h in temp:
            currH = res[-1][1]
            if h < 0:
                if abs(h) > currH:
                    res.append([i,abs(h)])
                cnt[abs(h)] = cnt[abs(h)] + 1 
                heapq.heappush(heights, -abs(h))
            elif h > 0:
                cnt[abs(h)]-=1
                if cnt[abs(h)] == 0 and abs(h) == currH:
                    # clean h
                    while cnt[-heights[0]] == 0:
                        heapq.heappop(heights)
                    res.append([i, -heights[0]])
        return res[1:]       
                
