class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 0 : return 0
        if len(heights) == 1 : return heights[0]
        j, m = 0, heights[0]
        for i in range(len(heights)):
            if  heights[i] < m: j, m = i, heights[i]
        a = m*len(heights)
        prev = -1
        for i in range(len(heights)):
            if heights[i] == m:
                a = max(a, self.largestRectangleArea(heights[prev+1:i]))
                prev = i
        a = max(a, self.largestRectangleArea(heights[prev+1:len(heights)]))
        return a
 
