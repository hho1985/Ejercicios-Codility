def solution (A,K):
    return (A[len(A) - K:len(A)] + A[0:len(A)- K])
    


A= [3,4,5,2]

print (solution(A,3))