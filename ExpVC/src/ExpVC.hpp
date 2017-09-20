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
//

/* Offers functionality to solve the vertex cover problem on undirected graphs
 *
 * Provides following functions (namespace vcexp):
 *
 * - void min_vertex_cover_exponential(G_t&, std::set<unsigned> &result)
 *
 */

#ifndef VCEXP
#define VCEXP

#include <set>
#include <vector>

#include <boost/graph/adjacency_list.hpp>

namespace vcexp{


template <typename G_t>
unsigned int min_vertex_cover_exponential(G_t &G, std::set<unsigned> &results)
{
    unsigned size = 0;

    return size;
}


} //namespace vcexp

#endif //VCEXP

// vim:ts=8:sw=4:et
