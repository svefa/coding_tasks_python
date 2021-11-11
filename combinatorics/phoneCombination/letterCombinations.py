  class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        d = {'2':"abc", '3':"def", '4':"ghi", '5': "jkl", '6':"mno", '7': "pqrs", '8':"tuv", '9':"wxyz" }
        if len(digits)==1: 
            return d[digits[0]]
        res = []
        return [letters+a for a in d[digits[-1]] for letters in self.letterCombinations(digits[:-1]) ]
             