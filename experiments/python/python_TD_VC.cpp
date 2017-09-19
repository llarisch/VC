// Lukas Larisch, 2017
//
// (c) 2017 King Abdullah University of Science and Technology
//
// This program is free software; you can redistribute it and/or modify it
// under the terms of the GNU General Public License as published by the
// Free Software Foundation; either version 2, or (at your option) any
// later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program; if not, write to the Free Software
// Foundation, 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
//

#include <boost/tuple/tuple.hpp>
#include <map>

#include <boost/graph/adjacency_list.hpp>
#include "./../../TD_VC/nice_decomposition.hpp"
#include "./../../TD_VC/applications.hpp"


typedef boost::adjacency_list<boost::setS, boost::vecS, boost::undirectedS> TD_graph_t;
typedef boost::adjacency_list<boost::vecS, boost::vecS, boost::undirectedS> TD_graph_vec_t;
typedef boost::adjacency_list<boost::vecS, boost::vecS, boost::directedS> TD_graph_directed_vec_t;
typedef boost::adjacency_list<boost::vecS, boost::vecS, boost::undirectedS, treedec::bag_t> TD_tree_dec_t;
typedef boost::adjacency_list<boost::vecS, boost::vecS, boost::bidirectionalS, treedec::bag_t> TD_tree_dec_directed_t;

#include "python_tdlib.hpp"


template <typename G_t>
void make_tdlib_graph(G_t &G, std::vector<unsigned int> &V, std::vector<unsigned int> &E, bool directed=false){
    unsigned int max = 0;
    for(unsigned int i = 0; i < V.size(); i++){
        max = (V[i]>max)? V[i] : max;
    }

    std::vector<typename boost::graph_traits<G_t>::vertex_descriptor> idxMap(max+1);
    for(unsigned int i = 0; i < V.size(); i++){
        idxMap[i] = boost::add_vertex(G);
    }

    if(E.size() != 0){
        for(unsigned int j = 0; j < E.size()-1; j++){
            boost::add_edge(idxMap[E[j]], idxMap[E[j+1]], G);
            if(directed){
                boost::add_edge(idxMap[E[j+1]], idxMap[E[j]], G);
            }
            j++;
        }
    }
}


template <typename T_t>
void make_tdlib_decomp(T_t &T, std::vector<std::vector<int> > &V, std::vector<unsigned int> &E){
    std::vector<typename T_t::vertex_descriptor> idxMap(V.size()+1);

    for(unsigned int i = 0; i < V.size(); i++){
        idxMap[i] = boost::add_vertex(T);
        std::set<unsigned int> bag;
        for(unsigned int j = 0; j < V[i].size(); j++){
            bag.insert(V[i][j]);
        }
        T[idxMap[i]].bag = bag;
    }

    if(E.size() != 0){
        for(unsigned int j = 0; j < E.size()-1; j++){
            boost::add_edge(idxMap[E[j]], idxMap[E[j+1]], T);
            j++;
        }
    }

}

template <typename G_t>
void make_python_graph(G_t &G, std::vector<unsigned int> &V_G, std::vector<unsigned int> &E_G,
                       bool ignore_isolated_vertices=false)
{
    typename boost::graph_traits<G_t>::vertex_iterator vIt, vEnd;
    for(boost::tie(vIt, vEnd) = boost::vertices(G); vIt != vEnd; vIt++){
        if(ignore_isolated_vertices && boost::degree(*vIt, G) == 0){
            continue;
        }
        V_G.push_back(*vIt);
    }

    typename boost::graph_traits<G_t>::edge_iterator eIt, eEnd;
    for(boost::tie(eIt, eEnd) = boost::edges(G); eIt != eEnd; eIt++){
        E_G.push_back(boost::source(*eIt, G));
        E_G.push_back(boost::target(*eIt, G));
    }
}


template <typename T_t>
void make_python_decomp(T_t &T, std::vector<std::vector<int> > &V_T,
                        std::vector<unsigned int> &E_T)
{
    std::map<typename boost::graph_traits<T_t>::vertex_descriptor, unsigned int> vertex_map;
    typename boost::graph_traits<T_t>::vertex_iterator tIt, tEnd;
    unsigned int id = 0;
    
    for(boost::tie(tIt, tEnd) = boost::vertices(T); tIt != tEnd; tIt++){
        vertex_map.insert(std::pair<typename boost::graph_traits<T_t>::vertex_descriptor, unsigned int>(*tIt, id++));
        std::vector<int> bag;
        for(std::set<unsigned int>::iterator sIt = T[*tIt].bag.begin(); sIt != T[*tIt].bag.end(); sIt++){
            bag.push_back(*sIt);
        }
        V_T.push_back(bag);
    }
    
    typename boost::graph_traits<T_t>::edge_iterator eIt, eEnd;
    for(boost::tie(eIt, eEnd) = boost::edges(T); eIt != eEnd; eIt++){
        typename std::map<typename boost::graph_traits<T_t>::vertex_descriptor, unsigned int>::iterator v, w;
        v = vertex_map.find(boost::source(*eIt, T));
        w = vertex_map.find(boost::target(*eIt, T));
        E_T.push_back(v->second);
        E_T.push_back(w->second);
    }
}



void gc_min_vertex_cover_with_treedecomposition(std::vector<unsigned int> &V_G, std::vector<unsigned int> &E_G,
                                                std::vector<std::vector<int> > &V_T, std::vector<unsigned int> &E_T,
                                                std::vector<unsigned int> &VC, unsigned graphtype)
{
    TD_tree_dec_t T;
    make_tdlib_decomp(T, V_T, E_T);

    TD_tree_dec_directed_t T_;
    treedec::make_rooted(T, T_);

    treedec::nice::nicify(T_);

    std::set<unsigned int> result;

    if(graphtype == 0){
        TD_graph_t G;
        make_tdlib_graph(G, V_G, E_G);

        treedec::app::min_vertex_cover_with_treedecomposition(G, T_, result);
    }
    else if(graphtype == 1){
        TD_graph_vec_t G;
        make_tdlib_graph(G, V_G, E_G);

        treedec::app::min_vertex_cover_with_treedecomposition(G, T_, result);
    }
    else{
        assert(false);
    }

    VC.resize(result.size());
    unsigned int i = 0;
    for(std::set<unsigned int>::iterator sIt = result.begin(); sIt != result.end(); sIt++){
        VC[i++] = *sIt;
    }
}

// vim:ts=8:sw=2:et
