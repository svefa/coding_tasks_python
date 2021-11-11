class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0: return [""]
        if n == 1: return ["()"]
        res=[]
        for p in self.generateParenthesis(n-1):
            res.append("()" + p)
            res.append("("+p+")")
        for i in range(1,n-1): # i = 1
            for q in self.generateParenthesis(i):
                for p in self.generateParenthesis(n-1-i):  # 3-1-1 = 1
                    res.append ("("+ q +")" + p )
        return res
        