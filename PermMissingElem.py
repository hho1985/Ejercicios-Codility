
def solution(A):
    if len(A) == 0:
        return 1
    ord = sorted(A)

    ultima= (ord[-1])
    
    b = range(ultima+1)

    return (sum(b) - sum(ord))


A=[]
print(solution(A))


"""Otra solucion


def function (A):
    ord = sorted(A)
    ultima= (ord[-1])
    B= range(1,ultima+1)
    faltantes=[]

    for i in B:
        if i not in A:
            faltantes.append(i)

    for i in faltantes:
        print (i)
    




A=[1,2,5]
function(A)