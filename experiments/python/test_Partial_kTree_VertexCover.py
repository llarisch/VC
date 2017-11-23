import base
import sys
import tdlib
import unittest
import time

if(len(sys.argv)<2 or sys.argv[1]!="long"):
    sys.exit(77)

from graphs import *
import Partial_kTrees

#don't confuse python unittest
sys.argv=sys.argv[:1]

PREFIX = "Partial_kTrees"

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

        COUNT = 0

        #for k in range(1, 16):
        for n in [50,100,200,250,500]:
            max_n2 = 0
            avg_n2 = 0.0

            max_m2 = 0
            avg_m2 = 0.0

            max_vc2 = 0
            avg_vc2 = 0.0

            max_tw2 = 0
            avg_tw2 = 0.0

            max_time2 = 0
            avg_time2 = 0.0

            Ns2 = list()
            Ms2 = list()
            VCs2 = list()
            TWs2 = list()
            TIMEs2 = list()

            COUNT2 = 0

            #for n in [50,100,200,250,500]:
            for k in range(1, 16):
                for p in [.97, .95, .90, .80, .70]:
                    for c in range(5):
                        suffix = str(n) + '_' + str(k) + '_' + str(p).replace('.','') + '_' + str(c)
                        #print(suffix)

                        G = Graph(eval(PREFIX+".V_"+suffix), eval(PREFIX+".E_"+suffix))


                        start = time.time()
                        #T, w = tdlib.minDegree_decomp(G)
                        T, w = tdlib.PP_FI_TM(G)
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

                        COUNT += 1

                        max_n2 = len(G.vertices()) if len(G.vertices()) > max_n2 else max_n2
                        avg_n2 += len(G.vertices())
                        Ns2.append(len(G.vertices()))

                        max_m2 = len(G.edges()) if len(G.edges()) > max_m2 else max_m2
                        avg_m2 += len(G.edges())
                        Ms2.append(len(G.edges()))

                        max_vc2 = s if s > max_vc2 else max_vc2
                        avg_vc2 += s
                        VCs2.append(s)

                        max_tw2 = w if w > max_tw2 else max_tw2
                        avg_tw2 += w
                        TWs2.append(w)

                        max_time2 = t if t > max_time2 else max_time2
                        avg_time2 += t
                        TIMEs2.append(t)


                        COUNT2 += 1

            avg_n2 /= COUNT2
            avg_m2 /= COUNT2
            avg_vc2 /= COUNT2
            avg_tw2 /= COUNT2
            avg_time2 /= COUNT2

            med_n2 = median(Ns2)
            med_m2 = median(Ms2)
            med_vc2 = median(VCs2)
            med_tw2 = median(TWs2)
            med_time2 = median(TIMEs2)

            print("---k: " + str(k) + "---")

            print("avg n: " + str(avg_n2))
            print("med n: " + str(med_n2))
            print("max n: " + str(max_n2))

            print("")

            print("avg m: " + str(avg_m2))
            print("med m: " + str(med_m2))
            print("max m: " + str(max_m2))

            print("")

            print("avg tw: " + str(avg_tw2))
            print("med tw: " + str(med_tw2))
            print("max tw: " + str(max_tw2))

            print("")

            print("avg vc: " + str(avg_vc2))
            print("med vc: " + str(med_vc2))
            print("max vc: " + str(max_vc2))

            print("")

            print("avg time: " + str(avg_time2))
            print("med time: " + str(med_time2))
            print("max time: " + str(max_time2))

        #COUNT = 1752-1224

        print("---total---")

        avg_n /= COUNT
        avg_m /= COUNT
        avg_vc /= COUNT
        avg_tw /= COUNT
        avg_time /= COUNT

        med_n = median(Ns)
        med_m = median(Ms)
        med_vc = median(VCs)
        med_tw = median(TWs)
        med_time = median(TIMEs)

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
