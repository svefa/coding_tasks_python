from typing import List
# Write any import statements here

def getMaxVisitableWebpages(N: int, L: List[int]) -> int:
  # Write your code here
   # Write your code here
  L = [0] + L
  Visited = [0]*(N+1)
  print(L)
  for i in range(N+1):
    cnt, j  = 0, i
    while Visited[j] == 0:
      cnt += 1
      print(j,"cnt", cnt)  
      Visited[j] = -1

      j=L[j]
      
      
    K = Visited[j] if Visited[j] > 0 else 0
    print("j,K", j, K)
    j = i

    while cnt > 0:
      Visited[j] = cnt + K
      print(j, "visited", Visited)   

      j = L[j]
      cnt -= 1
 
  print(Visited)
  return max(Visited)

#res = getMaxVisitableWebpages(4,[ 4, 1, 2, 1])
#print(res, 4) 

#res = getMaxVisitableWebpages(5,[4, 3, 5, 1, 2])
#print(res, 3) 

#res = getMaxVisitableWebpages(5,[ 2, 4, 2, 2, 3])
#print(res, 4) 

res = getMaxVisitableWebpages(3,[2, 3, 1])