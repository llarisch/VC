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

class TestTD_VC(unittest.TestCase):
    def test_max_clique(self):
        print("---max_clique---")

        max_vc = 0
        avg_vc = 0.0
        max_time = 0
        avg_time = 0.0

        for n in [50,100,200,250,500]:
            for k in range(1, 16):
                for p in [.97, .95, .90, .80, .70]:
                    for c in range(5):
                        suffix = str(n) + '_' + str(k) + '_' + str(p).replace('.','') + '_' + str(c)

                        base.print_graph_name(PREFIX, suffix)
                        G = Graph(eval(PREFIX+".V_"+str(suffix)), eval(PREFIX+".E_"+str(suffix)))

                        start = time.time()
                        T, w = tdlib.minDegree_decomp(G)
                        S = tdlib.max_clique_with_treedecomposition(G, T)
                        end = time.time()

                        t = end-start

                        max_vc = len(S) if len(S) > max_vc else max_vc
                        avg_vc += len(S)

                        max_time = t if t > max_time else max_time
                        avg_time += t

        avg_vc /= COUNT
        avg_time /= COUNT

        print("max clique: " + str(max_vc))
        print("avg clique: " + str(avg_vc))
        print("max time: " + str(max_time))
        print("avg time: " + str(avg_time))

if __name__ == '__main__':
    unittest.main()
