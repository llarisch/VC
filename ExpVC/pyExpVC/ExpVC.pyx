
from libcpp.vector cimport vector

from Graph import Graph


##############################################################
############ GRAPH/DECOMPOSITION ENCODING/DECODING ###########
#the following will be used implicitly do the translation
#between the python graph encoding and TdLib graph encoding,
#which is based on the BGL.

cdef cython_make_tdlib_graph(pyV, pyE, vector[unsigned int] &V, vector[unsigned int] &E):
    labels_map = list()
    labels_dict_inv = dict()

    for i in range(0, len(pyV)):
        V.push_back(i)
        labels_map.append(pyV[i])
        labels_dict_inv[pyV[i]] = i

    if len(pyE) > 0:
        #tuple representation
        if isinstance(pyE[0], tuple):
            for u,v in pyE:
                E.push_back(labels_dict_inv[u])
                E.push_back(labels_dict_inv[v])

        #list representation
        elif isinstance(pyE[0], list):
            for e in pyE:
                E.push_back(labels_dict_inv[e[0]])
                E.push_back(labels_dict_inv[e[1]])

        #internal representation (unfolded tuple/list representation)
        elif isinstance(pyE[0], int):
            for e in pyE:
                E.push_back(labels_dict_inv[e])

    return labels_map


def apply_labeling(X, labels_map):
    X_ = list()
    if len(X) > 0:
        #X is a list of vertices/edges
        if isinstance(X[0], int):
            for x in X:
                X_.append(labels_map[x])
        #X is a list of bags
        if isinstance(X[0], list):
            for x in X:
                 Y = list()
                 for x_ in x:
                     Y.append(labels_map[x_])
                 X_.append(Y)

    return X_


def inverse_labels_dict(labels_map):
    inv_dict = dict()
    for i in range(0, len(labels_map)):
        inv_dict[labels_map[i]] = i
    return inv_dict

#do not change without modifying python_tdlib.cpp
def graphtype_to_uint(string):
    if string == "boost_graph_undirected":
        return 0
    elif string == "boost_graph_directed":
        return 1
    else:
        raise Exception


def min_vertex_cover_exponential(G, T):
    """
    Computes a minimum vertex cover.

    INPUTS:

    - G : input graph

    OUTPUT:

    - VC:    a minimal vertex cover in G

    EXAMPLES:

        VC = ExpVC.min_vertex_cover(G)
    """

    cdef vector[unsigned int] V_G, E_G, VC_

    labels_map = cython_make_tdlib_graph(G.vertices(), G.edges(), V_G, E_G)
    inv_labels_dict = inverse_labels_dict(labels_map)

    cdef unsigned graphtype = graphtype_to_uint(G.graphtype())

    gc_min_vertex_cover_exponential(V_G, E_G, VC_, graphtype);

    py_VC = []
    cdef i;
    for i in range(0, len(VC_)):
        pyVCi = VC_[i]
        py_VC.append(pyVCi)

    return py_VC


