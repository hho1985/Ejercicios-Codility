def binary(A, X):

    inicio =0
    fin = len(A)- 1
 

    while inicio <= fin:
        mid = (inicio + fin) //2
        if A[mid] == X:
            return mid

        elif  X < A[mid]:
            fin = mid -1

        else:
            inicio = mid +1

    return None


A= [1,2,3,4,5]
print (binary(A,3))