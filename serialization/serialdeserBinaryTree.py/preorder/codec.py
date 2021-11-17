class Codec:
    def serialize(self, root):
        """ Encodes a tree to a single string
        :type root:TreeNode
        """
        def rserialize(root, string):
            if root is None:
                string += '#,'
            else:
                string += str(root.val) + ','
                string = rserialize(root.left, string)
                string = rserialize(root.right, string)
            return string
        return rserialize(root, '')
    
    def deserialize(self, data):
        def rdeserialize(l):
            if l[0] == '#':
                l.pop(0)
                return None
            root = TreeNode (l[0])
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root
        q=data.split(',')
        root=rdeserialize(q)
        return root

