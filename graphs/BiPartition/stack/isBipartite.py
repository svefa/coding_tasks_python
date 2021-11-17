class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        C = {} # colors
        S = list(range(len(graph)))  # stack 0,1,2
        C[len(graph)-1] = 1
        V = set()
        while S:
            n = S.pop()
            if n in V: continue
            V.add(n)
            if n not in C: C[n]=1
            for nei in graph[n]:
                if nei in C:
                    if C[nei] == C[n]:
                        return False
                if nei in V: continue
                C[nei] = -C[n]
                S.append(nei)
        return True
                
