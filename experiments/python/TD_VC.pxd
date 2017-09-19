from libcpp.vector cimport vector
from libcpp cimport bool

cdef extern from "python_TD_VC.hpp":

    void gc_min_vertex_cover_with_treedecomposition(vector[unsigned int] &V_G, vector[unsigned int] &E_G,
                                                    vector[vector[int]] &V_T, vector[unsigned int] &E_T,
                                                    vector[unsigned int] &VC, unsigned graphtype)

