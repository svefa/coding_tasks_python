class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        indices1 = [[nums1[i], i] for i in range(n)]
        indices2 = [[nums2[i], i] for i in range(n)]
        
        indices1.sort()
        indices2.sort()
        i1, i2, i3 = 0,0, n-1 
        # could be already result
        d = {}

        while i1 < n and i2 < n:
            if indices1[i1][0] > indices2[i2][0]:
                d[indices1[i1][1]] = indices2[i2][1]
                i1 += 1
                i2 += 1
            else:
                d[indices1[i1][1]] = indices2[i3][1]
                i1 += 1
                i3 -= 1 
        res = [-1]*n

        for k in d:
            v = d[k]
            res[v]=nums1[k]
        return res
            
            
        
        