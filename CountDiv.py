def solution (A,B,K):

    C = range(A,B+1)
    count=0
    for i in C:
        if i%K == 0:

            count+=1

    return count


print (solution(6,11,2))

"""Mejor rendimiento

def solution (A,B,K):

    if B==A:
        return 1

    if A%K==0:
        return (B-A) //K +1

    if A%K > 0:
        return (B-A) //K 