import base
import sys
import tdlib
import unittest
import time

if(len(sys.argv)<2 or sys.argv[1]!="long"):
    sys.exit(77)

from graphs import *
import Zoo

#don't confuse python unittest
sys.argv=sys.argv[:1]

PREFIX = "Zoo"
COUNT = 149

def median(L):
    L = sorted(L)
    return L[len(L)/2]

class TestTD_VC(unittest.TestCase):
    def test_min_vertex_cover(self):
        print("---vertex_cover---")

	max_n = 0
        avg_n = 0.0

	max_m = 0
        avg_m = 0.0

	max_vc = 0
        avg_vc = 0.0

	max_tw = 0
        avg_tw = 0.0

        max_time = 0
        avg_time = 0.0

        Ns = list()
        Ms = list()
        VCs = list()
        TWs = list()
        TIMEs = list()

        skip = 0

        cnt = 0

        for i in range(0, COUNT+1):
            base.print_graph_name(PREFIX, i)
            G = Graph(eval(PREFIX+".V_"+str(i)), eval(PREFIX+".E_"+str(i)))

            """
            T2, w2 = tdlib.minDegree_decomp(G)

            T3, w3 = tdlib.exact_decomposition_ex17(G)
            """

            start = time.time()
            T, w = tdlib.PP_FI_TM(G)


            print("...width " + str(w))
            """
            if w != w2 or w != w3:
                print("w1: " + str(w))
                print("w2: " + str(w2))
                print("w3: " + str(w3))
            """

            if w <= 20 or w > 27:
                print("......skip")
                skip += 1
                continue

            cnt+=1

            s, S = tdlib.min_vertex_cover_with_treedecomposition2(G, T, False)
            end = time.time()

            t = end-start

            max_n = len(G.vertices()) if len(G.vertices()) > max_n else max_n
            avg_n += len(G.vertices())
            Ns.append(len(G.vertices()))

            max_m = len(G.edges()) if len(G.edges()) > max_m else max_m
            avg_m += len(G.edges())
            Ms.append(len(G.edges()))

            max_vc = s if s > max_vc else max_vc
            avg_vc += s
            VCs.append(s)

            max_tw = w if w > max_tw else max_tw
            avg_tw += w
            TWs.append(w)

            max_time = t if t > max_time else max_time
            avg_time += t
            TIMEs.append(t)

        avg_n /= (COUNT - skip)
        avg_m /= (COUNT - skip)
        avg_vc /= (COUNT - skip)
        avg_tw /= (COUNT - skip)
        avg_time /= (COUNT - skip)

        med_n = median(Ns)
        med_m = median(Ms)
        med_vc = median(VCs)
        med_tw = median(TWs)
        med_time = median(TIMEs)

        print("#: " + str(cnt))

        print("avg n: " + str(avg_n))
        print("med n: " + str(med_n))
        print("max n: " + str(max_n))

        print("")

        print("avg m: " + str(avg_m))
        print("med m: " + str(med_m))
        print("max m: " + str(max_m))

        print("")

        print("avg tw: " + str(avg_tw))
        print("med tw: " + str(med_tw))
        print("max tw: " + str(max_tw))

        print("")

        print("avg vc: " + str(avg_vc))
        print("med vc: " + str(med_vc))
        print("max vc: " + str(max_vc))

        print("")

        print("avg time: " + str(avg_time))
        print("med time: " + str(med_time))
        print("max time: " + str(max_time))

if __name__ == '__main__':
    unittest.main()
