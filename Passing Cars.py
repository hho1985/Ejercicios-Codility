def solution (A):

    count = 0
    pos =0

    for i in A:
        pos+=1
        if i ==0:
            

            for j in A[pos:]:
                if j == 1:
                    count = count +1
