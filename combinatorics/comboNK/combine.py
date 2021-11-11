
def combine( n: int, k: int) :
    if n == k: return [[i for i in range(1,n+1)]]
    if k == 0: return [[]] 
    return combine(n-1, k) + [ c+[n] for c in combine(n-1,k-1)]

x = combine( 5,3)
print(x)
