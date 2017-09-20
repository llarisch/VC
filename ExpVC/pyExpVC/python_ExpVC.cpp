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
#include "../src/ExpVC.hpp"


typedef boost::adjacency_list<boost::setS, boost::vecS, boost::undirectedS> set_graph_t;
typedef boost::adjacency_list<boost::vecS, boost::vecS, boost::undirectedS> vec_graph_t;

#include "python_ExpVC.hpp"


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


void gc_min_vertex_cover_exponential(std::vector<unsigned int> &V_G, std::vector<unsigned int> &E_G,
                                                std::vector<unsigned int> &VC, unsigned graphtype)
{
    std::set<unsigned> result;

    if(graphtype == 0){
        set_graph_t G;
        make_tdlib_graph(G, V_G, E_G);

        vcexp::min_vertex_cover_exponential(G, result);
    }
    else if(graphtype == 1){
        vec_graph_t G;
        make_tdlib_graph(G, V_G, E_G);

        vcexp::min_vertex_cover_exponential(G, result);
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
