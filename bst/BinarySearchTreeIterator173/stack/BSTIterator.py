class BSIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = [root]

        while self.stack[-1].left: self.stack.append(stack[-1])

    def next(self) -> int:
        it = self.stack.pop()

        if it.right:
            self.stack.append(it.right)
            while self.stack[-1].left: 
                self.stack.append(self.stack[-1].left)
        return it.val

    def hasNext(self)->bool:
        return len(self.stack)

