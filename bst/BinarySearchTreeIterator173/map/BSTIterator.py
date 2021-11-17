# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.map = {}
        def dfs(node):
            a,b,c,d = node,node,node,node 
            if node.left: 
                a, b = dfs(node.left)
            if node.right: 
                c, d = dfs(node.right)
            if b != node: self.map[b] = node
            if c != node: self.map[node] = c
            return (a,d)
        a,b = dfs(root)
        self.ptr = a
        

    def next(self) -> int:
        a = self.ptr
        self.ptr =  self.map[self.ptr] if self.ptr in self.map else None
        return a.val

    def hasNext(self) -> bool:
        return self.ptr != None
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()