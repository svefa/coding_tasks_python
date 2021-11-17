from typing import List
# Write any import statements here

def getMaxVisitableWebpages(N: int, M: int, A: List[int], B: List[int]) -> int:
  # Write your code here
  N = N+1
  gIn = [[] for _ in range(N)] 
  gOut = [[] for _ in range(N)]
  In = [0]*N
  Out = [0]*N
  for i in range(M):
    gOut[A[i]].append(i)
    gIn[B[i]].append(i)
    In[B[i]] +=1
    Out[A[i]] +=1 
  # spanning
  #print("in ", In)
  #print("out", Out)
  q = []
  for i in range(N):
    if  In[i] == 0 or Out[i] == 0:
      q.append(i)
  #print("q", q)
  e = set()
  v = set()
  while q:
    i = q.pop()
    v.add(i)
    #print (i, "ginout", gOut[i]+gIn[i])
    for j in (gOut[i] + gIn[i]):
        #print(j)
        if j not in e:
            #print(j)
            e.add(j)
            In [B[j]] -= 1
            Out [A[j]] -= 1
            if In[B[j]] == 0: 
                q.append(B[j])
            if Out[A[j]] == 0:
                q.append(A[j])
  """
  print("in ", In)
  print("out", Out)

  print("e", e)   
  print("v", v)   
  """
  p=list(range(N))
  r=[0]*N
  
  def find(i):
    while i != p[i]:
      i = p[i]
    return i

  def union(i,j):
    pi, pj = find(i), find(j)
    if pi != pj:
      p[pi] = pj
  # r[pj] = r[pi] + r[pj]
  # union  

  for i in range(M):
    if i not in e:
      #print(i, A[i],B[i])  
      union(A[i], B[i])
 ##     print(r)
  # update rank
  #print("p", p)
  #print("r", r)

# count rank
  for i in range(N):
    pi = find(i)
    p[i] = pi
    r[pi] += 1
  #print("r", r)
# update rank for all
  #print("p", p) 
  for i in range(N):
    pi = find(i)
    r[i] = r[pi]

  #print("r", r)  
  p2 = set(p)
  In2 = {x:0 for x in p2}
  Out2 = {x:0 for x in p2}
  e2 = set()
  dp = {x:r[x]  for x in p2}

  while e:
    i = e.pop()

    pa, pb = find(A[i]), find(B[i])
    if (pa,pb) not in e2:
        e2.add((pa,pb))
        In2[pb] += 1
        Out2[pa] +=1

  for i in range(len(p2)+1):
        cnt = 0
        #print()
        dp2 = {x:r[x]  for x in p2}
        for a2,b2 in e2:
            dp2[b2] = max(dp2[b2], dp[a2] + r[b2])
            #print(i, ":", a2, b2,"dp2", dp2)
        if dp2 == dp :
            break
        dp = dp2
      
  """
  print("p2", p2 )
  print("e2", e2 )
  print("in2 ", In2)
  print("out2", Out2)
  print("out2", Out2)
  print("dp", dp)
"""
  return max(dp.values())  





N = 10
M = 9
#    
A = [3, 2, 5, 9, 10, 3, 3, 9, 4]
B = [9, 5, 7, 8, 6,  4, 5, 3, 9]

"""
3-> 9
3 -> 4
"""

r = getMaxVisitableWebpages(N, M, A, B)
print("answer", r, 5)

N = 4
M = 4
A = [1, 2, 3, 4]
B = [4, 1, 2, 1]

r = getMaxVisitableWebpages(N, M, A, B)
print("answer", r, 4)

N = 5
M = 6
A = [3, 5, 3, 1, 3, 2]
B = [2, 1, 2, 4, 5, 4]

r = getMaxVisitableWebpages(N, M, A, B)
print("answer", r, 4)