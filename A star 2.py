#https://www.mygreatlearning.com/blog/a-search-algorithm-in-artificial-intelligence/

def aStarAlgo(start_node, stop_node):
    open_set = set(start_node)
    closed_set = set()
    g = {}  # store distance from starting node
    parents = {}  # parents contains an adjacency map of all nodes

    # ditance of starting node from itself is zero
    g[start_node] = 0
    # start_node is root node i.e it has no parent nodes
    # so start_node is set to its own parent node
    parents[start_node] = start_node

    while len(open_set) > 0:
        n = None

        # node with lowest f() is found
        for v in open_set:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n == stop_node or Graph_nodes[n] == None:
            pass
        else:
            for (m, weight) in get_neighbors(n):
                # nodes 'm' not in first and last set are added to first
                # n is set its parent
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight


                # for each node m,compare its distance from start i.e g(m) to the
                # from start through n node
                else:
                    if g[m] > g[n] + weight:
                        # update g(m)
                        g[m] = g[n] + weight
                        # change parent of m to n
                        parents[m] = n

                        # if m in closed set,remove and add to open
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

        if n == None:
            print('Path does not exist!')
            return None

        # if the current node is the stop_node
        # then we begin reconstructin the path from it to the start_node
        if n == stop_node:
            path = []

            while parents[n] != n:
                path.append(n)
                n = parents[n]

            path.append(start_node)

            path.reverse()

            print('Path found: {}'.format(path))
            return path

        # remove n from the open_list, and add it to closed_list
        # because all of his neighbors were inspected
        open_set.remove(n)
        closed_set.add(n)

    print('Path does not exist!')
    return None


# define fuction to return neighbor and its distance
# from the passed node
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None


# for simplicity we ll consider heuristic distances given
# and this function returns heuristic distance for all nodes
# def heuristic(n):
#     H_dist = {
#         'A': 11,
#         'B': 6,
#         'C': 99,
#         'D': 1,
#         'E': 7,
#         'G': 0,
#
#     }
#
#     return H_dist[n]
#
#
# # Describe your graph here
# Graph_nodes = {
#     'A': [('B', 2), ('E', 3)],
#     'B': [('C', 1), ('G', 9)],
#     'C': None,
#     'E': [('D', 6)],
#     'D': [('G', 1)],
#
# }
# aStarAlgo('A', 'G')


# heuristik: luftlinie von jedem Punkt zu Endknoten
# distance code benutzen und statt lon2 und lat2 immer die Werte vom Endknoten eingeben
import math
import coordinates as c
import parse_csv as pc

# lon1 = -87.6828811088
# lon2 = -87.6746939239
# lat1 = 42.0123782948
# lat2 = 42.0126564502


"""https://www.kompf.de/gps/distcalc.html"""
"""Returns the distance from node 1 to node 2; e.g. edge 0, 26 to 27"""

lon2 = -87.6051897028
lat2 = 41.7512528176
def get_distance(lon1, lat1,):
    lat = (lat1 + lat2) / 2 * 0.0174533
    dx = 111.3 * math.cos(lat) * (lon1 - lon2)
    dy = 111.3 * (lat1 - lat2)
    dist_in_km = math.sqrt(dx * dx + dy * dy)
    dist_in_mi = dist_in_km * 0.62137
    return dist_in_mi


"""Returns distances from all connections (edges) in a list"""


def get_distance_list():
    lst = c.get_coordinates()
    par = pc.parse_csv()
    ls = []
    ls1 = dict()
    for i in range(len(lst)):
        lat = (lst[i][1] + lat2) / 2 * 0.0174533
        dx = 111.3 * math.cos(lat) * (lst[i][0] - lon2)
        dy = 111.3 * (lst[i][1] - lat2)
        dist_in_km = math.sqrt(dx * dx + dy * dy)
        dist_in_mi = dist_in_km * 0.62137
        ls.append(dist_in_mi)
        ls1[par[i].get("from")] = dist_in_mi
    return ls1


"""Returns distance from node 1 to node 2; input is the edge number (<=> index)"""


def get_edge_num_dist(num):
    return get_distance_list()[num]

print(get_distance(-87.6828811088, 42.0123782948,))
print(get_distance_list())

def heuristic(n):
    H_dist = get_distance_list()
    return H_dist[n]

Graph_nodes =
