class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [(root, False)]
        result = []
        while stack:
            current, sig = stack.pop()
            if current:
                if sig:
                    result.append(current.val)
                else:
                    stack.append((current.right, False))
                    stack.append((current, True))
                    stack.append((current.left, False))
        return result
                
   