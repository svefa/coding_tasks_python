def isMatch(text,pattern):
    dp = [[False]* (len(pattern) + 1) for _ in range(len(text) +1)] 
    dp[-1][-1] = True
    for i in range(len(text), -1, -1):
        for j in range(len(pattern) -1, -1, -1):
            match0=False
            if i < len(text):
                if pattern[j] == "." or pattern[j] == text[i]:
                    match0=True
            if j+1 < len(pattern) and pattern[j+1] == "*":
                if dp[i][j+2]==True: dp[i][j] = True
                elif match0 and dp[i+1][j]: dp[i][j] = True
            else:
                dp[i][j] = match0 and dp[i+1][j+1]
    return dp[0][0]