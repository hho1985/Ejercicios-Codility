def solution(X, Y, D):
    distancia = Y - X
    
    if distancia % D == 0:
        return distancia//D
        
    else:
        return distancia//D + 1