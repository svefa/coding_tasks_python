from typing import List
def merge(a,b):
    i, j = 0, 0
    res = []
    while i < len(a) and j < len(b):
        if a[i] < b[j] : 
            res.append(a[i])
            i+=1
        else :
            res.append(b[j])
            j +=1
    while i < len(a):
        res.append(a[i])
        i+=1
    while j < len(b):
        res.append(b[j])
        j+=1
    return res    

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        l=1
        while l < len(nums):
            i = 0
            while i < len(nums):
                nums[i:i+2*l] = merge(nums[i:i+l], nums[i+l:i+2*l])
                i += 2*l
            l *= 2        
        return nums
 
 
print(Solution().sortArray([1,2,4,4,5,3,1]))
