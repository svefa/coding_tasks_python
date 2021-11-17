def isMatch(text, pattern):
    memo={}
    def dp(i,j):
        if (i,j) not in memo:
            memo[(i,j)]=0
            if j == len(pattern):
                if i == len(text): memo[(i,j)] = True
                else: memo[(i,j)] = False
            else:
                match0 = False
                if i < len(text): 
                    if pattern[j] == text[i] or pattern[j] == '.': 
                        match0 = True
                if j+1 < len(pattern) and pattern[j+1] =='*':
                    memo[(i,j)] = dp(i, j+2) or (match0 and dp(i+1,j))
                else: 
                    memo[(i,j)] = match0 and dp(i+1,j+1) 
        return memo[(i,j)]
    return dp(0,0)

