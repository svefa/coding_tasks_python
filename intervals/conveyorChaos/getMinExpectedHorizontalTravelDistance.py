from typing import List
# Write any import statements here

class Interval:
  def __init__(self, x1, x2, height):
    self.height = height
    self.x1 = x1
    self.x2 = x2
    self.Left = None
    self.Right = None
    self.LeftRandomRight = (0.5, 0.5)
    self.Aggregation = None
  def Len(self):
    return self.x2-self.x1
  def Mid(self):
    return (self.x2+self.x1)/2
  def LenShift(self, x):
    return (self.x2-x)* self.LeftRandomRight[1] + (-self.x1+x)* self.LeftRandomRight[0] 
  def LeftRatio(self):
    if not self.Left: return None
    return self.x1 -self.Left.x1,  self.Left.x2 -self.x1
  def RightRatio(self):
    if not self.Right: return None
    return self.x2 -self.Right.x1,  self.Right.x2 -self.x2
  def Aggregate(self, x):
    if self.Aggregation != None: 
        return self.Aggregation
    L, R = 0.0, 0.0
    if self.Left != None: L = self.Left.Aggregate(self.x1)
    if self.Right != None: R = self.Right.Aggregate(self.x2)
    self.Aggregation =  L * self.LeftRandomRight[0] + R * self.LeftRandomRight[1] + self.LenShift(x)
    print("Aggr  (", L, "*", self.LeftRandomRight[0], "+", self.LenShift(x), "+", R, "*", self.LeftRandomRight[1], ") =", self.Aggregation )
    return self.Aggregation
  def TopAggregate(self):
    if self.Aggregation != None: 
        return self.Aggregation
    L, R = 0.0, 0.0
    if self.Left != None: L = self.Left.Aggregate(self.Mid())
    if self.Right != None: R = self.Right.Aggregate(self.Mid())
    self.Aggregation =  (L * self.LeftRandomRight[0] + R * self.LeftRandomRight[1])*self.Len()
    print("Top  (", L, "*", self.LeftRandomRight[0], "+", R, "*", self.LeftRandomRight[1], ")*", self.Len() , "=" ,self.Aggregation)
    return self.Aggregation
  def Print(self):
      print("H", self.height, "A", self.x1, "B", self.x2, "Aggregation", self.Aggregation)
      if self.Left != None: 
          print("    Left",  "H", self.Left.height, "A", self.Left.x1, "B", self.Left.x2, "Aggregation", self.Left.Aggregation)
      if self.Right != None: 
          print("    Right",  "H", self.Right.height, "A", self.Right.x1, "B", self.Right.x2, "Aggregation", self.Right.Aggregation)

def getMinExpectedHorizontalTravelDistance(N: int, H: List[int], A: List[int], B: List[int]) -> float:
    results = []
    res = helper(N, H, A, B, -1, True)
    for i in range(N):
        res = helper(N, H, A, B, i, True)
        results.append(res)
        res = helper(N, H, A, B, i, False)
        results.append(res)
        print(results)
    return min(results)

def helper(N: int, H: List[int], A: List[int], B: List[int], index: int, leftOrRight: bool) -> float:
    INF = 10**6
  # Write your code here
  #N = 5
  #H = [2, 8, 5, 9, 4]
  #A = [5000, 2000, 7000, 9000, 0]
  #B = [7000, 8000, 11000, 11000, 4000]
    """
    [2]  <-  ([3] (9,11):  9)  -> [*]
    [4]  <-  ([1] (2,8):   8)  -> [2]
    [*]  <-  ([2] (7, 11)  5)  -> [*]    
    [*]  <-  ([4] (0,4)    4)  -> [*]
    [*]  <-  ([0] (5,7)    2)  -> [*]
    """
    I=[]
    for i in range(N):
      I.append(Interval(A[i],B[i],H[i]))
      if i == index:
          if leftOrRight:
              I[i].LeftRandomRight = (0, 1.0)
          else:
              I[i].LeftRandomRight = (1.0, 0)

    I.sort(key = lambda x: -x.height)
    
    

    for i in range(N):
        for j in range(i+1,N):
            if I[i].height == I[j].height : 
                continue
            if I[j].x1 < I[i].x1 < I[j].x2:
                I[i].Left = I[j]
                break
        for j in range(i+1,N):
            if I[i].height == I[j].height : 
                continue
            if I[j].x1 < I[i].x2 < I[j].x2:
                I[i].Right = I[j]
                break
    
    for i in range(N):
        I[i].Aggregate(I[i].Mid())
    
    for i in range(N):
        I[i].Print()

    X = [0.0,INF] + A + B

    X.sort()
    print(X)

    TopI = []
    for i in range(1,len(X)):
        TopI.append(Interval (X[i-1], X[i], 10**6))
        mid = (TopI[-1].x1 + TopI[-1].x2)/2
        for j in range(N):
             if I[j].x1 < mid  < I[j].x2:
                TopI[-1].Left = I[j]
                TopI[-1].Right = I[j]
                break
    
    for t in TopI:
        t.TopAggregate()

    for t in TopI:
        t.Print()
    
    return (sum([t.Aggregation for t in TopI] ))/INF


       
N = 2
H = [10, 20]
A = [100000, 400000]
B = [600000, 800000]
res = getMinExpectedHorizontalTravelDistance(N, H, A, B) 
print("res:",res,", expected:",155000)

N = 5
H = [2, 8, 5, 9, 4]
A = [5000, 2000, 7000, 9000, 0]
B = [7000, 8000, 11000, 11000, 4000]
res = getMinExpectedHorizontalTravelDistance(N, H, A, B) 
print("res:",res,", expected:",36.50000000)
