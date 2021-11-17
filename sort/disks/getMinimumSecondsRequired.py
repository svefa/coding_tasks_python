from typing import List
# Write any import statements here

def getMinimumSecondsRequired(N: int, R: List[int], A: int, B: int) -> int:
  # Write your code here
  cost = {}
  d = [ (i+1) -R[i] for i in range(N)]
  cost = [max(d[i]*A, -d[i]*B) for i in range(N)]
  neg = sum ([int(d[i] < 0) for i in range(N)])
  pos = sum ([d[i] >= 0 for i in range(N)])
  #print("cost", cost)
  #print("d", d)
  #print ("neg:", neg, "pos:", pos )
  for i in range(N) :
    print("d", d)
    print("i, d[i] , neg, B , pos, A:   ", i, d[i] , neg, B , pos, A)
    while d[i] < 0 and neg*B > pos*A: 
      cost1 = sum([max(d[i]*A, -d[i]*B) for i in range(N)])
      print("cost", cost1)  

      for j in range(i, N):
        d[j] += 1
        if d[j] == 0:
          pos += 1
          neg -= 1
      cost2 = sum([max(d[i]*A, -d[i]*B) for i in range(N)])
      print("cost2", cost2, "neg:", neg, "pos:", pos )  
 
    if d[i] >= 0: 
       neg -= 1 
    else : pos -= 0
  print("d", d)    
  cost =  sum([max(d[i]*A, -d[i]*B) for i in range(N)])
    
  
  
  
  return cost

N = 3
R = [100, 100, 100]
A = 2
B = 3

#res = getMinimumSecondsRequired(N, R, A, B) 
#print("res:", res, ", exp:", 5)

N = 6
R = [6, 5, 2, 4, 4, 7]
A = 1
B = 1
res = getMinimumSecondsRequired(N, R, A, B) 
print("res:", res, ", exp:", 10)