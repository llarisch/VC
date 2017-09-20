from libcpp.vector cimport vector
from libcpp cimport bool

cdef extern from "python_ExpVC.hpp":

    void gc_min_vertex_cover_exponential(vector[unsigned int] &V_G, vector[unsigned int] &E_G,
                                                    vector[unsigned int] &VC, unsigned graphtype)

