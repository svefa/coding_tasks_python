def isMatch(text, pattern) :
    if not pattern:
        return not text
    
    match0 = False
    if text: match0 = (pattern[0] == text[0] or pattern == '0')
    
    if len(pattern) >=2 and pattern[1] == "*":
        return isMatch(text, pattern[2:]) or (match0 and isMatch(text[1:], pattern))
    
    return match0 and isMatch(text[1:], pattern[1:])
