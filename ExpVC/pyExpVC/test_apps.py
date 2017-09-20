import base
import sys
import unittest
import random
import ExpVC

from Graph import Graph as Graph
from graphs import *

#don't confuse python unittest
sys.argv=sys.argv[:1]

class TestTD_VC(unittest.TestCase):
    def test_min_vertex_cover_exp_0a(self):
        V, E = cornercases[0]
        G = Graph(V, E)
        S = ExpVC.min_vertex_cover_exponential(G)
        self.assertEqual(len(S), 0)

    def test_min_vertex_cover_exp_0b(self):
        V, E = cornercases[1]
        G = Graph(V, E)
        S = ExpVC.min_vertex_cover_exponential(G)
        self.assertEqual(len(S), 0)

    def test_min_vertex_cover_exp_0c(self):
        V, E = cornercases[2]
        G = Graph(V, E)
        S = ExpVC.min_vertex_cover_exponential(G)
        self.assertEqual(len(S), 0)

    def test_min_vertex_cover_exp_0d(self):
        V, E = cornercases[3]
        G = Graph(V, E)
        S = ExpVC.min_vertex_cover_exponential(G)
        self.assertEqual(len(S), 4)

    def test_min_vertex_cover_exp_1(self):
        G = Graph(V_P6, E_P6)
        S = ExpVC.min_vertex_cover_exponential(G)
        self.assertEqual(len(S), 3)

    def test_min_vertex_cover_exp_2(self):
        G = Graph(V_K5, E_K5)
        S = ExpVC.min_vertex_cover_exponential(G)
        self.assertEqual(len(S), 4)

    def test_min_vertex_cover_exp_3(self):
        G = Graph(V_Petersen, E_Petersen)
        S = ExpVC.min_vertex_cover_exponential(G)
        self.assertEqual(len(S), 6)

    def test_min_vertex_cover_exp_4(self):
        G = Graph(V_Petersen_double, E_Petersen_double)
        S = ExpVC.min_vertex_cover_exponential(G)
        self.assertEqual(len(S), 12)

    def test_min_vertex_cover_exp_5(self):
        G = Graph(V_Wagner, E_Wagner)
        S = ExpVC.min_vertex_cover_exponential(G)
        self.assertEqual(len(S), 5)

    def test_min_vertex_cover_exp_6(self):
        G = Graph(V_Pappus, E_Pappus)
        S = ExpVC.min_vertex_cover_exponential(G)
        self.assertEqual(len(S), 9)

    def test_min_vertex_cover_exp_7(self):
        G = Graph(V_Grid_5_5, E_Grid_5_5)
        S = ExpVC.min_vertex_cover_exponential(G)
        self.assertEqual(len(S), 12)

    def test_min_vertex_cover_exp_8(self):
        for n in range(0, 13):
            for i in range(0, 10):
                V, E = randomGNP(n, 0.2)
                G = Graph(V, E)
                S = ExpVC.min_vertex_cover_exponential(G)

if __name__ == '__main__':
    unittest.main()
