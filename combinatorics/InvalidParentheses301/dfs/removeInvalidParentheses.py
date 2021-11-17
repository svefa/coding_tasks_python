class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = set()
        def dfs(s,res):
            #print (s,res)
            c1 = 0
            o =[]
            for i in range(len(s)):
                if s[i]=="(": 
                    c1 +=1
                    
                if s[i] == ")":
                    c1 -=1 
                    o.append(i)
                    if (c1 == -1):
                        for j in o:
                            if j-1 not in o:
                                dfs(s[:j]+s[j+1:],res)
                        return
            c2 = 0
            c =[]
            for i in range(len(s)-1,-1,-1):
                if s[i]==")": 
                    c2 +=1
                    
                if s[i] == "(":
                    c2 -=1
                    c.append(i) 
                    if (c2 == -1):
                        for j in c :
                            if j+1 not in c:
                                dfs(s[:j]+s[j+1:],res)
                        return
            res.add(s)
        dfs(s,res)
        return res
        
        