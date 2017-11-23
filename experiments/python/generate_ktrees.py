import random
import copy

def k_tree(n, k, p):
    if k+1 >= n:
        print("invalid choice of n,k")
        return

    V = range(n)
    E = [[i, j] for i in range(k+1) for j in range(i+1, k+1)]
    C = [range(k+1)]

    for i in range(k+1, n):
        idx = random.randint(0, len(C)-1)
        nextC = list()
        while len(nextC) < k:
            r = random.randint(0, len(C[idx])-1)
            if C[idx][r] in nextC:
                continue
            nextC.append(C[idx][r])

        for j in range(0, k):
            E.append([i,nextC[j]])

        nextC.append(i)
        C.append(copy.deepcopy(nextC))


    E_ = list()
    for i in range(0, len(E)):
        r = random.randint(0, 1000000)
        if r < p*1000000:
            E_.append(E[i])



    return V, E_
            


fout = open("Partial_kTrees.py", 'w')
for n in [50,100,200,250,500]:
    avg = 0.0
    for k in range(1, 16):
        for p in [.97, .95, .90, .80, .70]:
            for c in range(5):
                V, E = k_tree(n, k, 1.0-p)
                #print(str(V))
                #print(str(E))

                suffix = str(n) + '_' + str(k) + '_' + str(p).replace('.','') + '_' + str(c)

                fout.write("V_"+suffix+" = " + str(V) + '\n')
                fout.write("E_"+suffix+" = " + str(E) + '\n')
                fout.write("name_"+suffix+" = "+'\"'+suffix+'\"'+ '\n')
                #print(str(len(E)))
                avg+=len(E)
                fout.write('\n')

    #print("avg: " + str(avg/(15*5*5)))
fout.close()


