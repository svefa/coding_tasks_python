from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1 : return [nums]
        return [ p[:i] + [nums[-1]] + p[i:]  for i in range(len(nums)) for p in self.permute(nums[:-1])]
 