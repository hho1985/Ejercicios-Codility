def solution (N,A):
    counters = [0] * N
    max1=0

    for x in A:
        if x >= 1 and x <= N:
            counters [x-1]+=1

            if counters [x-1] > max1:
                max1 = counters [x-1]

        else:
            counters = [max1] * N

    return counters


A=[3,4,4,6,1,4,4]

print (solution(1,A))