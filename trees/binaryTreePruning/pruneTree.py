
# 814. Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def pruneTree(root):
    if not root: return None
    root.Left = pruneTree(root.left)
    root.Right = pruneTree(root.right)
    if root.val == 0 and not root.left and not root.right: root=None
    return root


