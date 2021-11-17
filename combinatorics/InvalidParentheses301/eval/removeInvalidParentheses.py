def removeInvalidParentheses(s):
    def isvalid(s):
        ctr = 0
        for c in s:
            if c == '(':
                ctr += 1
            elif c == ')':
                ctr -= 1
                if ctr < 0:
                    return False
        return ctr == 0
    level = {s}
    while True:
        valid = list(filter(isvalid, level))
        if valid:
            return valid
        level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}

s = "()()()"
ans = removeInvalidParentheses("()())()")

print(ans)
