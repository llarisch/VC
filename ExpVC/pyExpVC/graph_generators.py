#random graphs
def randomGNP(n, p):
    import random
    V = []
    E = []
    for i in range(0, n):
        V.append(i)
        for j in range(i+1,n):
            if random.randint(0, 100) <= p*100:
                E.append((i, j))
    return V, E
