# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 1 x 2 3
        a=[]
        stack = [root]
        # 1
        while stack[-1]:
            stack.append(stack[-1].left)
        stack.pop()
        while stack:
            a.append(stack[-1].val)
            stack[-1] = stack[-1].right
            while stack[-1] :
                stack.append(stack[-1].left)
            stack.pop()
        return a
