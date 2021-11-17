from typing import List
# Write any import statements here
# DOESNOT WORK

def getMaxVisitableWebpages(N: int, L: List[int]) -> int:
  # Write your code here
  # [0, 4, 3, 5, 1, 2]
   # Write your code here
  L = [0] + L
  Visited = [0]*(N+1) 
  
  def dfs(i):
    if Visited[i] > 0: 
      pass
    elif Visited[i] == -1: 
      Visited[i] = 1
    else :
      Visited[i]=-1
      j = L[i]
      if Visited[j] == 0 : 
        dfs(j)
        Visited[i] = Visited[j]+1
      elif Visited[j] == -1: 
        L[i]=i
        Visited[i] = 1
      else: 
        Visited[i] = Visited[j]+1
              
  for i in range(N+1):
    dfs(i)
      
  return max(Visited)

res = getMaxVisitableWebpages(4,[ 4, 1, 2, 1])
print(res, 4) 

res = getMaxVisitableWebpages(5,[4, 3, 5, 1, 2])
print(res, 3) 

res = getMaxVisitableWebpages(5,[ 2, 4, 2, 2, 3])
print(res, 4) 

res = getMaxVisitableWebpages(3,[2, 3, 1])
print(res, 3)

