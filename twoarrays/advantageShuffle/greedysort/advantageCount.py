def advantageCOunt(A,B):
    A = deque(sorted(A))
    for b,i in sorted([b,i] for i,b in enumerate(B)):
        B[i] = A.pop() if -b < A[-1] else A.popleft()
    return B