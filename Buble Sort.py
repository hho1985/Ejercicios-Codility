def ordenar(A):
    index = len(A)-1
    sorted = False

    while not sorted:
        sorted = True


        for i in range (0, index):

            if A[i] > A[i+1]:
                sorted = False

                A[i], A[i+1] = A[i+1], A[i]

    return A


A=[4,9,1,6,0]
print (ordenar(A))