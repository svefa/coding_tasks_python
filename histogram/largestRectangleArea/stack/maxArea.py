def largestRectangleArea(heights):
    heights.append(0)
    stack=[-1]
    a = 0
    for i in range(len(heights)):
        while heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i -stack[-1] - 1
            a = max(a, h*w)
        stack.append(i)
    heights.pop()
    return a
a=largestRectangleArea([1,2,5,2])
print(a)