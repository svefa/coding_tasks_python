from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def divideAndConquer(self, root: Optional[TreeNode], left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not root: return True
        if left and left.val >= root.val : return False
        if right and root.val >= right.val: return False
        if not self.divideAndConquer(root.left, left, root) : return False
        if not self.divideAndConquer(root.right, root, right) : return False
        return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
         return self.divideAndConquer(root, None, None)
    
        