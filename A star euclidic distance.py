#https://www.mygreatlearning.com/blog/a-search-algorithm-in-artificial-intelligence/
import duration
import test



def aStarAlgo(start_node, stop_node):
    open_set = {start_node} # set(start_node)
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

        print(n)

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



# heuristik: luftlinie von jedem Punkt zu Endknoten
# distance code benutzen und statt lon2 und lat2 immer die Werte vom Endknoten eingeben
import math
import coordinates as coo
import parse_csv as pc
import distance as dis
import get_predicted_duration_new as gpd


lat2 = 41.7512528176
lon2 = -87.6051897028


def get_distance_list():
    lst = coo.get_coordinates()
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
    return ls


def heuristic(n):
    H_dist = get_distance_list()
    return H_dist[int(n)]


# constructing graph
per = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0037, 0.0037, 0.0077,
       0.0077, 0.0077, 0.0077, 0.0077, 0.023, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
       0.0, 0.0, 0.0, 0.0, 0.0, 0.0237, 0.0237, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
       0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0002, 0.0, 0.0,
       0.0, 0.0, 0.0, 0.0042, 0.0042, 0.0042, 0.0042, 0.0042, 0.0042, 0.0042, 0.027, 0.0506, 0.0, 0.0, 0.0, 0.0002,
       0.0408, 0.0, 0.2908, 0.0, 0.0506, 0.0438, 0.0, 0.0173, 0.0, 0.0, 0.0, 0.0527, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0237,
       0.0, 0.0, 0.0002, 0.0, 0.0007, 0.0019, 0.0, 0.0, 0.0656, 0.0, 0.0, 0.0, 0.0, 0.0005, 0.0005, 0.0, 0.0, 0.0,
       0.003, 0.003, 0.0, 0.0, 0.0949, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0007, 0.0007, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
       0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0649, 0.1289, 0.1289, 0.1537, 0.1537, 0.1537, 0.0206, 0.0, 0.0, 0.0, 0.0, 0.0,
       0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0042, 0.063, 0.0007, 0.0, 0.0014, 0.0007, 0.0, 0.0, 0.0007, 0.0, 0.0,
       0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0005, 0.0005, 0.0, 0.0, 0.0, 0.0602, 0.0, 0.0148, 0.0551, 0.0, 0.0846,
       0.0, 0.0, 0.0905, 0.0202, 0.0084, 0.2105, 0.0, 0.0, 0.0, 0.0452, 0.0, 0.0, 0.0, 0.0028, 0.0, 0.4654, 0.0, 0.0122,
       0.0, 0.0005, 0.1455, 0.0, 0.0, 0.0, 0.0059, 0.0, 0.0, 0.0, 0.0, 0.011, 0.0277, 0.1455, 0.0, 0.0, 0.0935, 0.0368,
       0.0, 0.0098, 0.0262, 0.0452, 0.6285, 0.0, 0.0, 0.0002, 0.0, 0.0028, 0.0091, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0874, 0.0,
       0.3131, 0.0, 0.6285, 0.0206, 0.027, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0098, 0.0014, 0.0005, 0.0, 0.2147,
       0.0028, 0.0007, 0.0, 0.0237, 0.2641, 0.1411, 0.0, 0.0989, 0.0, 0.0009, 0.0227, 0.0, 0.0, 0.0696, 0.0098, 0.0,
       0.0014, 0.0, 0.0, 0.0, 1.0, 0.0007, 0.0293, 0.0026, 0.4617, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.023, 0.0007, 0.0,
       0.0026, 0.0, 0.0, 0.0002, 0.0129, 0.8378, 0.0, 0.011, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0091, 0.0642, 0.0,
       0.0, 0.0, 0.0, 0.0077, 0.2641, 0.3122, 0.6691, 0.0, 0.0, 0.0045, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0084, 0.0293, 0.0002,
       0.0, 0.0, 0.0, 0.0, 0.0457, 0.0293, 0.0, 0.0, 0.0262, 0.0, 0.0, 0.0, 0.0, 0.0352, 0.0014, 0.0084, 0.0005, 0.0516,
       0.0098, 0.0757, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0098, 0.0, 0.1111, 0.0019, 0.0295, 0.0, 0.0028, 0.4654, 0.0112,
       0.0312, 0.0, 0.0, 0.0012, 0.2112, 0.0, 0.2112, 0.6285, 0.0, 0.0, 0.0005, 0.0905, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0098,
       0.0, 0.0, 0.0, 0.0, 0.7345, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0553, 0.6285, 0.0, 0.0, 0.0, 0.0183, 0.0005, 0.0183,
       0.0197, 0.0277, 0.0, 0.011, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0696, 0.1455, 0.1029, 0.0026, 0.0, 0.0042, 0.0012, 0.1155,
       0.0, 0.0, 0.0, 0.0335, 0.011, 0.0, 0.0, 0.6285, 0.2105, 0.0281, 0.0, 0.0, 0.0905, 0.0, 0.0, 0.0, 0.0183, 0.0,
       0.0262, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0708, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.7345, 0.0, 0.2105, 0.0262,
       0.1008, 0.8378, 0.0084, 0.0288, 0.0002, 0.0042, 0.023, 0.0, 0.0103, 0.0, 0.0, 0.0227, 0.0, 0.0, 0.0, 0.0005,
       0.0288, 0.0337, 0.0007, 0.0, 0.0, 0.0197, 0.0042, 0.0028, 0.0, 0.0, 0.0, 0.0028, 0.0, 0.0, 0.0, 0.1029, 0.0,
       0.1174, 0.8378, 0.0026, 0.0166, 0.0129, 0.0, 0.0923, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.6285,
       0.0, 0.0042, 0.0, 0.0, 0.0028, 0.003, 0.0, 0.0103, 0.0, 0.0, 0.0, 0.1411, 0.0007, 0.0, 0.0042, 0.0, 0.0, 0.0295,
       0.0162, 0.0375, 0.0, 0.0096, 0.0, 0.8378, 0.0206, 0.0, 0.0, 0.0, 0.1455, 0.0, 0.0, 0.0, 0.0506, 0.0, 0.0, 0.0258,
       0.0002, 0.0045, 0.0, 0.0293, 0.0905, 0.0, 0.0077, 0.0, 0.0197, 0.0, 0.0197, 0.0, 0.0162, 0.0178, 0.0173, 0.0014,
       0.0042, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0009, 0.0, 0.0, 0.0, 0.3122, 0.0, 0.0009, 0.0, 0.0, 0.0002,
       0.0408, 0.0, 0.0, 0.153, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0227, 0.0, 0.3131, 0.0178, 0.2641, 0.0,
       0.0977, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0696, 0.0452, 0.0, 0.0, 0.0005, 0.0, 0.0, 0.0, 0.018, 0.0012, 0.0, 0.0,
       0.0, 0.0, 0.0, 0.6285, 0.0, 0.0173, 0.0506, 0.0, 0.0, 0.0, 0.0002, 0.0, 0.0, 0.0, 0.0, 0.0047, 0.0293, 0.0005,
       0.3122, 0.0, 0.0, 0.0, 0.0005, 0.0, 0.0, 0.0, 0.0, 0.0047, 0.2641, 0.2105, 0.0028, 0.0, 0.0, 0.0007, 0.0009,
       0.0209, 0.0, 0.0935, 0.0, 0.0, 0.0033, 0.2641, 0.0, 0.0134, 0.0, 0.0, 0.0, 0.0042, 0.0005, 0.0197, 0.0068, 0.153,
       0.0, 0.1036, 0.0, 0.0014, 0.0551, 0.2105, 0.0, 0.6285, 0.0002, 0.0, 0.1111, 0.0, 0.0, 0.0002, 0.0206, 0.0211,
       0.0091, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0368, 0.0211, 0.0, 0.3436, 0.0, 0.0977, 0.2112, 0.0, 0.0002, 0.0084, 0.0063,
       0.0, 0.1158, 0.0295, 0.0002, 0.0, 0.0, 0.2339, 0.0, 0.0, 0.0, 0.0, 0.2112, 0.0183, 0.0, 0.0457, 0.0, 0.0, 0.0,
       0.0, 0.0206, 0.0002, 0.0178, 0.0014, 0.0005, 0.0, 0.0675, 0.0, 0.0, 0.0, 0.0166, 0.0, 0.0419, 0.0005, 0.0, 0.0,
       0.0, 0.0, 0.0, 0.0935, 0.011, 0.0007, 0.0, 0.0209, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4143, 0.0424, 0.0012, 0.0696,
       0.0, 0.0211, 0.0, 0.0, 0.0, 0.0084, 0.0, 0.0016, 0.0, 0.6285, 0.0, 0.0, 0.0, 0.0, 0.0094, 0.0, 0.0, 0.0, 0.0,
       0.0134, 0.0, 0.0, 0.0, 0.0, 0.0, 0.8378, 0.0, 0.1465, 0.0, 0.0007, 0.0, 0.0, 0.0, 0.1411, 0.0, 0.0237, 0.0, 0.0,
       0.0, 0.6285, 0.0, 0.0, 0.0, 0.0, 0.0262, 0.0237, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2105, 0.0, 0.0, 0.0457, 0.0091, 0.0,
       0.0, 0.0, 0.6285, 0.0098, 0.0, 0.153, 0.0, 0.0, 0.0, 0.138, 0.0, 0.3478, 0.2775, 0.0, 0.0, 0.0, 0.0, 0.0162,
       0.101, 0.0, 0.0, 0.0026, 0.0, 0.0007, 0.0, 0.0007, 0.0424, 0.0, 0.0, 0.0005, 0.0, 0.0258, 0.0, 0.0007, 0.0,
       0.0042, 0.0002, 0.0, 0.0, 0.0042, 0.0, 0.0, 0.1336, 0.0087, 0.0905, 0.0, 0.0012, 0.0, 0.0, 0.0002, 0.0, 0.0026,
       0.0, 0.0002, 0.0094, 0.0129, 0.0, 0.0, 0.0492, 0.0103, 0.0002, 0.0087, 0.0197, 0.0, 0.0, 0.0, 0.0012, 0.0,
       0.0007, 0.0, 0.0002, 0.0, 0.0675, 0.0002, 0.0783, 0.0202, 0.0, 0.0012, 0.0, 0.0, 0.0237, 0.0, 0.0, 0.0, 0.0, 0.0,
       0.0281, 0.3131, 0.0, 0.0014, 0.0, 0.2147, 0.0077, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0319, 0.0, 0.0, 0.0279, 0.3827,
       0.0, 0.4617, 0.0, 0.0, 0.0, 0.0005, 0.0891, 0.0, 0.0345, 0.0, 0.0134, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0349,
       0.0757, 0.0183, 0.0143, 0.0, 0.0, 0.034, 0.0279, 0.0014, 0.0, 0.7345, 0.0, 0.0, 0.0, 0.0103, 0.0, 0.0, 0.0, 0.0,
       0.0, 0.0, 0.0, 0.0, 0.0, 0.0098, 0.0, 0.6285, 0.0, 0.0084, 0.0, 0.0492, 0.0007, 0.0178, 0.0, 0.0, 0.0, 0.1411,
       0.0, 0.0103, 0.0007, 0.0, 0.0028, 0.0, 0.0, 0.2641, 0.0007, 0.0, 0.0607, 0.0, 0.0014, 0.0, 0.0, 0.0, 0.0246, 0.0,
       0.0, 0.0, 0.0, 0.0, 0.0173, 0.0033, 0.0, 0.0977, 0.0, 0.0, 0.0, 0.1901, 0.0, 0.0, 0.1174, 0.0, 0.6285, 0.0, 0.0,
       0.0, 0.0026, 0.0921, 0.0534, 0.0419, 0.0, 0.0, 0.0293, 0.0, 0.0005, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
       0.0237, 0.0696, 0.0, 0.0248, 0.0, 0.0, 0.0042, 0.0, 0.0, 0.0012, 0.0, 0.0, 0.0005, 0.0424, 0.0002, 0.0935, 0.0,
       0.0607, 0.0002, 0.0, 0.0206, 0.0197, 0.0, 0.0277, 0.0206, 0.0, 0.0, 0.0084, 0.0002, 0.0, 0.0, 0.0103, 0.0045,
       0.0, 0.0, 0.0, 0.0, 0.153, 0.0, 0.0, 0.0, 0.0007, 0.0, 0.0312, 0.0183, 0.0143, 0.0, 0.0, 0.0352, 0.0096, 0.0,
       0.0295, 0.0, 0.0237, 0.0, 0.8378, 0.0, 0.3715, 0.0, 0.0, 0.0129, 0.0933, 0.0, 0.0007, 0.0, 0.0237, 0.0, 0.0, 0.0,
       0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.6285, 0.0, 0.0002, 0.0014, 0.0, 0.0, 0.1411, 0.0, 0.0668, 0.0,
       0.0206, 0.0, 0.0134, 0.0, 0.0, 0.0, 0.0, 0.0424, 0.0, 0.0, 0.0, 0.0492, 0.153, 0.0, 0.1111, 0.0, 0.0, 0.0905,
       0.0122, 0.0295, 0.0, 0.0016, 0.0, 0.0, 0.0492, 0.0002, 0.0, 0.0162, 0.0173, 0.0, 0.0701, 0.0, 0.0, 0.3827, 0.0,
       0.1008, 0.0, 0.0, 0.0, 0.0457, 0.2147, 0.0, 0.0, 0.0, 0.0077, 0.0002, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0002, 0.0,
       0.0368, 0.0, 0.0, 0.0, 0.4617, 0.0091, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0696, 0.0, 0.0, 0.0, 0.003, 0.0, 0.0, 0.0122,
       0.0166, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0002, 0.2112, 0.0, 0.0, 0.0, 0.0783, 0.0, 0.3131, 0.0989, 0.3136,
       0.0, 0.0012, 0.0009, 0.0, 0.0, 0.0, 0.0005, 0.0319, 0.0, 0.0, 0.0005, 0.0007, 0.109, 0.0002, 0.0, 0.0002, 0.0,
       0.0045, 0.0005, 0.0, 0.0098, 0.0, 0.0037, 0.0298, 0.0, 0.0019, 0.0016, 0.0534, 0.1411, 0.0005, 0.2351, 0.3541,
       0.0084, 0.0005, 0.0244, 0.0, 0.0801, 0.0, 0.0, 0.0984, 0.019, 0.0, 0.0042, 0.0, 0.3136, 0.3143, 0.0, 0.0007, 0.0,
       0.0, 0.0002, 0.0014, 0.0045, 0.0, 0.0, 0.0, 0.0023, 0.0, 0.0511, 0.0, 0.1392, 0.0169, 0.0, 0.1162, 0.033, 0.0,
       0.4617, 0.131, 0.0, 0.0, 0.0, 0.0157, 0.0, 0.3274, 0.0, 0.0497, 0.0005, 0.1577, 0.2775, 0.0002, 0.0, 0.0152,
       0.0687, 0.0, 0.0]

Graph_nodes = dict()
p = pc.parse_csv()
counter = 0
liste = []
for i in range(1, len(p)):
    fro = p[i].get("from")
    if fro in liste:
        continue
    to = p[i].get("to")
    lst = []
    for j in range(counter, len(p)-1):
        if fro == p[j+1].get("from"):
            if per[i - 1] >= 0.40:
                percentage = 1-per[j]
            else:
                percentage = 1
            lst.append((str(p[j+1].get("to")), test.get_edges_predicted_duration_new('28 Mr 00_09_46')[j] * percentage))  # dis.get_edge_num_dist(j)
            if fro not in liste:
                liste.append(fro)
    counter += 1
    Graph_nodes[str(fro)] = lst
Graph_nodes['0'] = None


'''Graph_nodes = {'26': [('27', 1.2), ('39', 1.2)], '28': [('29', 1.13), ('27', 1.06)], '29': [('30', 1.37), ('28', 1.1)], '31': [('1', 2.15), ('32', 2.04)], '32': [('31', 2.02), ('33', 1.32)], '33': [('32', 1.31), ('34', 3.04)], '34': [('33', 2.56), ('35', 1.34)], '35': [('34', 1.26), ('397', 1.1)], '292': [('397', 0.43), ('408', 1.4), ('291', 3.34)], '408': [('292', 1.28), ('91', 1.07), ('36', 1.56)], '36': [('408', 1.56), ('37', 2.54)], '37': [('36', 2.54), ('38', 2.46)], '38': [('37', 2.51), ('39', 2.2800000000000002)], '39': [('38', 2.37), ('26', 1.1400000000000001)], '27': [('26', 1.22), ('28', 1.06)], '30': [('29', 1.29), ('251', 1.28)], '434': [('40', 1.37), ('40', 1.37), ('154', 1.46), ('262', 1.21)], '40': [('447', 1.3), ('447', 1.3)], '447': [('41', 1.44), ('41', 1.44), ('153', 1.29), ('327', 0.41)], '41': [('112', 0.39), ('112', 0.39)], '112': [('42', 0.43)], '42': [('43', 1.1), ('112', 0.43)], '43': [('480', 1.22), ('42', 1.1)], '480': [('44', 1.18), ('155', 1.25), ('43', 1.13), ('359', 1.25)], '44': [('480', 1.22), ('529', 1.1)], '448': [('45', 1.53), ('449', 1.52), ('93', 0.58), ('337', 1.03)], '46': [('47', 1.3900000000000001), ('75', 2.02)], '47': [('48', 1.01), ('46', 1.45)], '48': [('49', 0.43), ('47', 1.02)], '49': [('449', 1.43), ('48', 0.44)], '449': [('422', 2.08), ('49', 1.49), ('57', 1.49), ('448', 1.42)], '422': [('449', 1.5699999999999998), ('138', 1.05), ('396', 1.05)], '50': [('51', 1.51), ('55', 2.08)], '52': [('53', 1.43), ('54', 1.41)], '54': [('52', 2.22), ('55', 1.43)], '55': [('54', 2.25), ('50', 1.32)], '51': [('50', 2.35), ('241', 2.04)], '53': [('56', 3.23), ('52', 1.43)], '56': [('57', 1.44), ('53', 3.25)], '80': [('58', 2.52), ('73', 1.4), ('202', 2.46)], '58': [('59', 1.37), ('80', 3.23)], '59': [('58', 2.01), ('86', 1.22)], '60': [('450', 0.58), ('2', 1.18)], '450': [('60', 0.58), ('66', 0.35), ('130', 1.07), ('414', 1.11)], '75': [('61', 2.02), ('62', 1.55), ('46', 1.51)], '61': [('45', 2.02), ('75', 1.52)], '45': [('448', 2.04), ('61', 1.52)], '57': [('449', 1.43), ('56', 1.46)], '62': [('63', 1.53), ('75', 2.03)], '63': [('64', 1.07), ('62', 1.58)], '64': [('65', 0.57), ('63', 1.1)], '66': [('67', 0.34), ('450', 0.35)], '67': [('68', 1.03), ('66', 0.35)], '68': [('69', 1.44), ('67', 1.04)], '69': [('70', 0.41), ('68', 1.45)], '70': [('71', 0.28), ('69', 0.41)], '71': [('72', 3.38), ('70', 0.28)], '72': [('202', 1.22), ('71', 3.4)], '73': [('74', 1.13), ('80', 1.41)], '451': [('417', 0.44), ('16', 0.51), ('224', 1.22), ('247', 1.23)], '65': [('64', 0.59), ('130', 0.58)], '202': [('72', 1.23), ('80', 2.4699999999999998), ('203', 2.5)], '74': [('73', 1.16), ('143', 2.56)], '14': [('76', 0.16), ('392', 1.1400000000000001)], '76': [('14', 0.16), ('428', 0.35)], '77': [('430', 0.29), ('478', 1.15)], '430': [('77', 0.28), ('417', 1.13), ('418', 0.43)], '78': [('79', 1.02), ('109', 2.15)], '428': [('508', 0.59), ('442', 0.28), ('276', 1.06)], '436': [('452', 1.32), ('432', 1.47), ('475', 0.44)], '533': [('530', 0.39), ('387', 2.07), ('412', 1.44), ('412', 1.11), ('530', 0.34), ('532', 2.19)], '372': [('14', 0.29), ('515', 0.37), ('442', 0.23)], '392': [('372', 1.44), ('437', 0.46), ('518', 0.4)], '453': [('81', 1.28), ('124', 1.11), ('277', 1.21), ('226', 1.29)], '15': [('435', 1.1), ('516', 0.38)], '82': [('83', 1.25), ('81', 1.28)], '515': [('372', 0.34), ('445', 0.31), ('518', 2.11), ('528', 0.45)], '81': [('453', 1.31), ('82', 1.28)], '83': [('82', 1.22), ('85', 1.26)], '84': [('85', 0.45), ('510', 0.32)], '438': [('3', 0.27), ('528', 0.3), ('432', 1.44), ('528', 0.27)], '528': [('438', 0.31), ('172', 1.5699999999999998), ('515', 0.33), ('445', 0.45), ('25', 0.58), ('24', 1.32)], '87': [('88', 0.38), ('97', 1.54)], '88': [('451', 1.2), ('87', 0.43)], '417': [('451', 0.43), ('430', 1.12), ('229', 0.5)], '297': [('89', 1.2), ('114', 1.04), ('298', 1.43)], '89': [('90', 1.28), ('297', 1.17)], '90': [('89', 1.34), ('216', 0.19)], '91': [('92', 2.03), ('408', 1.07)], '2': [('60', 1.19)], '93': [('425', 1.07), ('448', 1.03)], '425': [('93', 1.04), ('331', 1.03), ('289', 2.07)], '3': [('438', 0.3)], '94': [('95', 0.56), ('209', 0.59)], '95': [('96', 1.01), ('94', 1.01)], '96': [('95', 1.29), ('8', 2.29)], '97': [('17', 1.49), ('87', 1.54)], '17': [('97', 1.46), ('127', 0.42)], '4': [('454', 1.18)], '454': [('4', 1.16), ('187', 1.1), ('374', 0.43), ('357', 1.06)], '455': [('98', 1.43), ('431', 1.3900000000000001), ('496', 1.22), ('324', 1.15)], '98': [('456', 1.54), ('455', 1.48)], '456': [('99', 2.08), ('98', 2.09), ('347', 0.58), ('238', 1.1)], '99': [('100', 2.09), ('456', 1.53)], '100': [('524', 2.17), ('99', 1.5899999999999999)], '457': [('101', 2.05), ('524', 1.54), ('481', 1.1), ('131', 1.5)], '101': [('102', 2.0), ('457', 2.05)], '102': [('103', 1.56), ('101', 2.0)], '103': [('104', 1.3), ('102', 1.56)], '104': [('105', 1.19), ('103', 1.3)], '105': [('18', 0.43), ('104', 1.19)], '524': [('100', 2.11), ('189', 1.3), ('457', 1.52), ('481', 1.32)], '18': [('105', 0.43), ('291', 0.53)], '5': [('106', 1.44)], '106': [('5', 2.19), ('216', 1.09)], '107': [('108', 1.08), ('111', 1.13)], '110': [('79', 1.1), ('345', 3.4)], '79': [('78', 1.05), ('110', 1.1)], '452': [('436', 1.3599999999999999), ('443', 0.41), ('172', 0.37), ('387', 0.35)], '536': [('516', 0.47), ('537', 0.46), ('437', 0.58), ('516', 1.03), ('537', 0.52), ('23', 1.11)], '516': [('536', 0.49), ('536', 0.59), ('234', 1.17), ('22', 0.29)], '531': [('113', 0.47), ('483', 1.17), ('534', 0.48), ('534', 0.5), ('488', 1.03)], '113': [('532', 1.28), ('531', 0.41)], '19': [('458', 0.34), ('506', 0.47)], '458': [('19', 0.35), ('295', 1.13), ('314', 1.01), ('506', 0.32)], '114': [('297', 1.04), ('280', 1.01)], '109': [('78', 2.05), ('341', 1.07)], '1': [('31', 2.16)], '397': [('292', 0.36), ('167', 1.1400000000000001), ('35', 0.58)], '115': [('459', 1.08), ('353', 1.15)], '423': [('116', 1.17), ('330', 1.1), ('121', 2.04)], '412': [('533', 1.43), ('529', 1.31), ('533', 1.26), ('419', 1.01)], '460': [('117', 1.17), ('306', 1.16), ('248', 1.19), ('279', 1.21)], '118': [('119', 1.19), ('137', 1.19)], '461': [('20', 0.49), ('523', 1.06)], '120': [('462', 1.3599999999999999), ('490', 1.41)], '121': [('423', 2.09), ('299', 2.26)], '415': [('122', 1.25), ('143', 2.09), ('146', 1.35)], '463': [('123', 1.29), ('359', 1.33), ('402', 1.02), ('309', 1.32)], '534': [('537', 0.48), ('537', 0.37), ('531', 0.52), ('531', 0.52), ('21', 1.09), ('477', 1.12)], '124': [('125', 1.02), ('453', 1.02)], '464': [('126', 1.44), ('342', 1.21), ('378', 1.2), ('162', 1.55)], '127': [('492', 1.17), ('471', 0.36)], '465': [('128', 0.49), ('273', 2.2800000000000002), ('298', 1.11), ('362', 1.02)], '511': [('129', 1.25), ('496', 1.18), ('407', 1.55), ('482', 2.2800000000000002)], '519': [('530', 1.1400000000000001), ('523', 0.38), ('483', 0.32)], '131': [('457', 1.5899999999999999), ('221', 1.3)], '132': [('133', 1.16), ('493', 1.06)], '134': [('135', 0.48), ('320', 1.09)], '517': [('136', 1.49), ('175', 1.4), ('305', 1.24), ('11', 1.28), ('164', 1.31), ('350', 1.15)], '466': [('137', 2.09), ('336', 1.31), ('339', 1.11), ('331', 1.04)], '529': [('412', 1.24), ('44', 1.28), ('160', 1.35), ('419', 0.49), ('403', 1.32)], '467': [('138', 0.55), ('349', 1.0), ('339', 1.17), ('337', 1.01)], '468': [('139', 1.44), ('264', 1.13), ('286', 1.09), ('346', 1.16)], '469': [('140', 1.08), ('156', 1.48), ('211', 1.22), ('459', 1.53)], '108': [('510', 1.25), ('107', 1.23)], '470': [('142', 1.06), ('154', 1.26), ('509', 2.58), ('235', 1.07)], '143': [('415', 2.16), ('74', 3.02)], '537': [('536', 0.38), ('534', 0.47), ('534', 0.45), ('536', 0.41), ('525', 1.08), ('435', 1.17)], '144': [('145', 1.46), ('383', 1.18)], '146': [('147', 1.3900000000000001), ('415', 1.23)], '439': [('471', 0.47), ('252', 0.37)], '148': [('472', 1.04), ('498', 1.25)], '149': [('150', 1.25), ('215', 1.16)], '151': [('473', 1.19), ('290', 0.35)], '140': [('152', 1.1), ('469', 1.18)], '474': [('153', 1.49), ('235', 1.23), ('416', 1.32), ('258', 1.27)], '154': [('434', 1.47), ('470', 1.22)], '155': [('480', 1.23), ('398', 0.55)], '157': [('476', 0.56), ('390', 1.07)], '21': [('534', 1.02), ('435', 0.48)], '158': [('159', 0.53), ('244', 0.35)], '129': [('160', 1.02), ('511', 1.3900000000000001)], '161': [('162', 1.43), ('405', 1.24)], '163': [('164', 1.16), ('166', 1.2)], '165': [('427', 1.06), ('240', 1.16)], '478': [('77', 1.23), ('247', 1.15), ('391', 1.22), ('316', 1.25)], '166': [('163', 1.3), ('307', 1.31)], '133': [('479', 1.13), ('132', 1.05)], '462': [('120', 1.28), ('310', 1.18), ('368', 1.21), ('404', 1.1400000000000001)], '167': [('168', 1.22), ('397', 0.5)], '169': [('170', 1.35), ('279', 1.3900000000000001)], '476': [('171', 1.05), ('310', 0.51), ('157', 0.51), ('201', 1.02)], '479': [('513', 1.01), ('135', 0.59), ('133', 1.06), ('218', 1.19)], '482': [('511', 2.29), ('496', 1.34), ('502', 1.41), ('520', 2.04)], '172': [('452', 0.32), ('438', 1.19)], '173': [('174', 0.39), ('275', 1.1)], '175': [('517', 1.56), ('521', 1.32)], '483': [('477', 0.36), ('526', 1.0), ('519', 0.38), ('531', 1.11)], '85': [('84', 0.49), ('83', 1.19)], '176': [('484', 1.35), ('333', 1.35)], '177': [('178', 1.33), ('116', 1.04)], '513': [('179', 1.1400000000000001), ('365', 1.21), ('188', 1.13), ('479', 1.0)], '180': [('181', 1.3599999999999999), ('373', 1.44)], '390': [('182', 1.13), ('208', 1.1), ('157', 1.08)], '183': [('184', 1.21), ('267', 1.19)], '185': [('186', 1.44), ('227', 1.37)], '485': [('188', 1.22), ('489', 1.51), ('184', 1.08), ('227', 1.28)], '189': [('190', 1.37), ('524', 1.31)], '472': [('191', 1.09), ('204', 1.25), ('243', 1.06), ('148', 1.03)], '192': [('193', 1.0), ('420', 1.15)], '194': [('486', 1.38), ('475', 1.3599999999999999)], '195': [('196', 0.45), ('484', 0.48)], '389': [('197', 1.15), ('361', 1.19), ('388', 1.3)], '198': [('147', 1.35), ('410', 1.25)], '199': [('200', 1.17), ('420', 1.07)], '487': [('201', 1.18), ('293', 1.26), ('302', 1.13), ('317', 1.1400000000000001)], '435': [('488', 1.38), ('23', 0.41), ('10', 1.09), ('537', 1.21)], '205': [('206', 1.29), ('294', 1.29)], '490': [('207', 1.19), ('286', 1.11), ('366', 2.31), ('120', 1.27)], '525': [('477', 0.45), ('437', 0.28), ('537', 1.07), ('518', 1.11)], '208': [('390', 1.04), ('358', 1.25)], '209': [('210', 0.57), ('94', 0.55)], '491': [('492', 1.23), ('501', 0.55), ('503', 3.5300000000000002), ('219', 1.3900000000000001)], '211': [('469', 1.11), ('219', 1.4)], '535': [('212', 1.34), ('497', 2.09), ('441', 0.54)], '213': [('214', 2.1), ('270', 2.32)], '419': [('529', 0.26), ('412', 0.55)], '493': [('413', 1.08), ('0', 0.56), ('394', 1.1), ('132', 1.17)], '217': [('426', 0.4), ('239', 0.36)], '489': [('218', 1.1400000000000001), ('311', 1.2), ('485', 1.47), ('338', 1.18)], '212': [('488', 1.32), ('535', 1.38)], '219': [('491', 1.5899999999999999), ('211', 1.34)], '494': [('220', 1.2), ('268', 1.35), ('257', 1.22), ('371', 1.16)], '486': [('194', 1.23), ('123', 1.15), ('403', 1.32), ('363', 1.3599999999999999)], '222': [('223', 1.28), ('344', 1.17)], '215': [('149', 1.16), ('236', 1.05)], '484': [('117', 1.3599999999999999), ('195', 0.42), ('176', 1.28), ('254', 1.27)], '7': [('225', 2.35)], '226': [('495', 1.31), ('453', 1.34)], '210': [('522', 1.13), ('209', 0.54)], '225': [('7', 2.24), ('251', 1.31)], '228': [('471', 1.23), ('16', 1.26)], '432': [('438', 1.25), ('436', 2.05), ('446', 1.15)], '229': [('230', 0.46), ('417', 0.49)], '231': [('171', 1.11), ('349', 0.59)], '232': [('233', 1.1400000000000001), ('340', 1.26)], '234': [('15', 0.34), ('332', 0.29)], '236': [('498', 1.17), ('215', 1.13)], '237': [('238', 1.29), ('495', 1.13)], '240': [('165', 1.13), ('281', 1.16)], '241': [('242', 0.4), ('51', 2.5300000000000002)], '224': [('451', 1.24), ('252', 0.48)], '446': [('445', 1.07), ('393', 1.29), ('508', 0.57), ('24', 0.37)], '245': [('246', 1.25), ('326', 1.19)], '499': [('9', 2.2), ('303', 2.27), ('362', 1.11), ('360', 1.03)], '248': [('249', 1.28), ('460', 1.2)], '250': [('520', 1.22), ('347', 0.41)], '251': [('225', 1.49), ('30', 1.2)], '252': [('439', 0.43), ('224', 0.41)], '253': [('500', 1.4), ('159', 1.5)], '130': [('450', 1.06), ('65', 1.0)], '254': [('255', 1.35), ('484', 1.31)], '501': [('256', 1.34), ('491', 0.53), ('492', 1.19), ('382', 1.24)], '257': [('494', 1.25), ('498', 1.25)], '502': [('520', 1.2), ('482', 1.46), ('367', 1.32), ('379', 1.35)], '258': [('473', 1.35), ('474', 1.28)], '92': [('259', 0.22), ('91', 1.46)], '496': [('431', 0.55), ('482', 1.45), ('511', 1.25), ('455', 1.33)], '260': [('261', 1.43), ('473', 1.42)], '262': [('249', 1.22), ('434', 1.28)], '125': [('124', 1.03), ('429', 0.57)], '263': [('497', 1.33), ('505', 1.11)], '265': [('266', 1.22), ('440', 1.05)], '267': [('183', 1.1), ('261', 1.55)], '503': [('491', 2.46), ('395', 1.12), ('512', 2.09), ('296', 1.33)], '145': [('144', 2.02), ('509', 2.36)], '191': [('269', 1.2), ('472', 1.1400000000000001)], '136': [('444', 1.33), ('517', 1.55)], '235': [('474', 1.28), ('470', 1.02)], '518': [('527', 0.38), ('525', 1.1), ('527', 0.34), ('6', 1.28)], '504': [('207', 1.29), ('343', 1.32), ('206', 1.04), ('424', 1.5899999999999999)], '271': [('272', 0.43), ('375', 0.46)], '272': [('274', 0.42), ('271', 0.44)], '275': [('173', 0.56), ('312', 0.26)], '276': [('364', 0.27), ('76', 0.18)], '277': [('278', 1.3900000000000001), ('453', 1.17)], '168': [('167', 1.1), ('285', 1.1)], '160': [('129', 1.05), ('529', 1.28)], '473': [('260', 1.35), ('244', 1.27), ('151', 1.19), ('258', 1.22)], '220': [('152', 1.07), ('494', 1.1400000000000001)], '281': [('282', 1.29), ('240', 1.15)], '283': [('440', 1.17), ('381', 1.08)], '196': [('195', 0.49), ('328', 1.34)], '230': [('229', 0.47), ('508', 0.57)], '508': [('428', 1.2), ('230', 1.04), ('442', 0.55), ('446', 0.54)], '138': [('467', 0.53), ('422', 1.01)], '10': [('435', 1.11)], '259': [('92', 0.25), ('384', 1.29)], '505': [('532', 1.13), ('488', 2.37), ('263', 1.11), ('407', 1.17)], '174': [('284', 1.04), ('173', 0.36)], '286': [('468', 1.11), ('490', 1.09)], '287': [('497', 1.23), ('356', 1.41)], '288': [('204', 1.22), ('338', 1.23)], '204': [('472', 1.25), ('288', 1.23)], '289': [('425', 2.01), ('320', 1.25)], '290': [('151', 0.31), ('509', 0.35)], '506': [('186', 1.31), ('458', 0.33), ('296', 1.28), ('304', 1.5899999999999999)], '498': [('236', 1.13), ('369', 1.15), ('148', 1.21), ('257', 1.16)], '291': [('292', 3.24), ('326', 1.13)], '471': [('127', 0.41), ('228', 1.2), ('439', 0.47), ('393', 1.28)], '294': [('205', 1.23), ('370', 1.34)], '295': [('459', 1.07), ('458', 1.1400000000000001)], '296': [('503', 1.29), ('506', 2.11)], '413': [('493', 1.12), ('414', 1.09), ('493', 1.06)], '218': [('479', 1.11), ('489', 1.16)], '477': [('527', 0.55), ('525', 0.43), ('534', 1.2), ('483', 0.38)], '150': [('507', 2.2), ('149', 1.24)], '427': [('300', 1.25), ('165', 1.1), ('399', 1.16)], '301': [('405', 1.13), ('386', 1.23)], '162': [('464', 1.37), ('161', 1.24)], '170': [('169', 1.31), ('348', 1.1)], '497': [('431', 2.33), ('535', 2.11), ('287', 1.25), ('263', 1.34)], '123': [('463', 1.37), ('486', 1.28)], '244': [('158', 0.37), ('473', 1.31)], '507': [('302', 1.28), ('150', 2.11), ('424', 1.33), ('404', 1.24)], '304': [('500', 2.03), ('506', 1.5)], '214': [('213', 2.14), ('520', 2.5)], '495': [('282', 1.08), ('226', 1.32), ('190', 1.15), ('237', 1.17)], '407': [('505', 1.07), ('511', 1.58), ('532', 1.1)], '306': [('307', 1.31), ('460', 1.2)], '137': [('118', 1.27), ('466', 2.03)], '243': [('308', 1.15), ('472', 1.13)], '159': [('253', 1.45), ('158', 0.52)], '309': [('500', 0.58), ('463', 1.32)], '305': [('517', 1.37), ('329', 1.38)], '387': [('452', 0.4), ('475', 1.25), ('12', 0.53)], '312': [('313', 0.38), ('275', 0.25)], '314': [('458', 1.08), ('308', 1.17)], '315': [('509', 2.4), ('203', 2.51)], '316': [('478', 1.35), ('411', 1.1400000000000001)], '509': [('470', 2.13), ('145', 2.1), ('290', 0.34), ('315', 2.58)], '523': [('461', 1.16), ('530', 1.13), ('526', 0.53), ('519', 0.32)], '420': [('192', 1.05), ('376', 1.1), ('199', 1.11)], '317': [('318', 0.59), ('487', 1.25)], '319': [('299', 0.53), ('355', 1.07)], '321': [('322', 1.22), ('269', 1.22)], '323': [('324', 1.28), ('278', 1.41)], '325': [('385', 1.13), ('377', 1.46)], '269': [('321', 1.19), ('191', 1.24)], '327': [('328', 1.49), ('447', 0.49)], '329': [('223', 1.16), ('305', 1.27)], '330': [('423', 1.03), ('358', 1.01)], '223': [('329', 1.29), ('222', 1.27)], '332': [('441', 0.43), ('234', 0.37)], '308': [('314', 1.07), ('243', 1.31)], '193': [('192', 1.01), ('300', 1.49)], '333': [('176', 1.43), ('367', 1.27)], '334': [('385', 1.12), ('421', 1.12)], '284': [('335', 1.33), ('174', 1.05)], '311': [('119', 1.2), ('489', 1.2)], '429': [('125', 0.4), ('426', 0.52), ('181', 1.47)], '318': [('336', 1.08), ('317', 1.06)], '322': [('293', 0.53), ('321', 1.24)], '337': [('467', 1.08), ('448', 1.04)], '164': [('163', 1.22), ('517', 1.33)], '339': [('466', 1.13), ('467', 1.21)], '147': [('146', 1.28), ('198', 1.23)], '141': [('510', 0.23), ('399', 1.1400000000000001)], '341': [('280', 1.13), ('109', 1.02)], '181': [('180', 1.5), ('429', 1.4)], '342': [('464', 1.19), ('514', 1.11)], '126': [('343', 1.3599999999999999), ('464', 1.38)], '344': [('222', 1.18), ('522', 1.13)], '521': [('175', 1.37), ('400', 1.1400000000000001), ('246', 1.28)], '270': [('444', 0.4), ('213', 2.38)], '216': [('106', 1.31), ('90', 0.2)], '152': [('220', 1.04), ('140', 1.16)], '345': [('110', 3.4), ('242', 3.14)], '227': [('485', 1.26), ('185', 1.29)], '346': [('433', 1.16), ('468', 1.08)], '186': [('185', 1.46), ('19', 0.48)], '256': [('501', 1.3), ('475', 1.3900000000000001)], '238': [('456', 1.16), ('237', 1.32)], '348': [('170', 1.1), ('122', 1.07)], '481': [('350', 1.29), ('444', 2.14), ('457', 1.06), ('524', 1.23)], '459': [('295', 1.1), ('469', 1.56), ('395', 1.13), ('115', 1.13)], '273': [('351', 2.55), ('465', 2.44)], '444': [('352', 2.09), ('481', 2.14), ('136', 1.3900000000000001), ('270', 0.37)], '207': [('504', 1.28), ('490', 1.22)], '119': [('118', 1.13), ('311', 1.16)], '274': [('272', 0.36), ('441', 1.16)], '405': [('301', 1.09), ('360', 1.03), ('161', 1.28)], '188': [('513', 1.11), ('485', 1.38)], '201': [('476', 1.05), ('487', 1.41)], '357': [('454', 1.04), ('128', 1.04)], '358': [('208', 1.09), ('330', 1.07)], '266': [('522', 3.08), ('265', 1.07)], '360': [('405', 1.05), ('499', 1.08)], '362': [('499', 1.1), ('465', 1.17)], '203': [('315', 2.41), ('202', 2.51)], '512': [('363', 1.11), ('382', 1.25), ('406', 1.35), ('503', 2.02)], '364': [('276', 0.28), ('392', 1.1400000000000001), ('516', 0.5)], '352': [('255', 1.24), ('444', 2.02)], '197': [('340', 1.4), ('389', 1.17)], '128': [('465', 0.52), ('357', 0.52)], '20': [('526', 1.2), ('25', 0.5)], '326': [('245', 1.16), ('18', 0.26)], '366': [('490', 2.17), ('514', 1.34)], '184': [('183', 1.12), ('485', 1.1)], '206': [('504', 1.04), ('205', 1.41)], '440': [('285', 1.25), ('283', 1.19), ('265', 1.19)], '242': [('241', 0.42), ('345', 3.5300000000000002)], '23': [('536', 1.1400000000000001), ('15', 0.35)], '335': [('284', 1.26), ('386', 1.22)], '182': [('390', 1.13), ('433', 1.2)], '433': [('368', 1.08), ('346', 1.08), ('182', 1.25)], '313': [('312', 0.4), ('409', 0.49)], '246': [('245', 1.35), ('521', 1.32)], '353': [('369', 1.19), ('115', 1.21)], '441': [('535', 0.51), ('332', 0.54), ('274', 1.13)], '356': [('287', 1.34), ('373', 1.26)], '370': [('371', 1.17), ('294', 1.19)], '347': [('250', 0.36), ('456', 1.09)], '200': [('199', 1.17), ('384', 0.17)], '374': [('454', 0.42), ('139', 1.1400000000000001)], '351': [('377', 1.31), ('273', 3.01)], '233': [('378', 1.16), ('232', 1.31)], '293': [('487', 1.17), ('322', 0.55)], '385': [('334', 1.07), ('325', 1.13), ('178', 1.11)], '380': [('381', 1.2), ('400', 1.26)], '340': [('232', 1.28), ('197', 1.32)], '349': [('467', 1.12), ('231', 1.01)], '365': [('383', 1.2), ('513', 1.17)], '384': [('200', 0.22), ('259', 1.31)], '135': [('134', 0.54), ('479', 0.59)], '361': [('389', 1.23), ('411', 1.21)], '117': [('484', 1.35), ('460', 1.31)], '475': [('387', 1.34), ('256', 1.37), ('194', 1.25), ('436', 0.47)], '388': [('389', 1.27), ('268', 0.56)], '302': [('487', 1.15), ('507', 1.38)], '369': [('353', 1.2), ('498', 1.16)], '377': [('351', 1.22), ('325', 1.45)], '156': [('469', 1.47), ('391', 0.32)], '391': [('478', 1.29), ('156', 0.35)], '522': [('266', 3.08), ('210', 1.06), ('344', 1.2), ('354', 1.3)], '371': [('494', 1.2), ('370', 1.2)], '426': [('375', 0.37), ('217', 0.38), ('429', 0.55)], '12': [('443', 0.42), ('533', 1.1)], '431': [('497', 1.58), ('455', 1.11), ('496', 0.54)], '393': [('446', 1.35), ('471', 1.31)], '116': [('177', 1.1), ('423', 1.15)], '190': [('189', 1.34), ('495', 1.32)], '375': [('271', 0.49), ('426', 0.35)], '171': [('231', 1.12), ('476', 1.13)], '86': [('59', 2.01), ('142', 1.02)], '298': [('297', 1.47), ('465', 1.13)], '300': [('193', 1.53), ('427', 1.32)], '279': [('169', 1.3), ('460', 1.23)], '381': [('380', 1.2), ('283', 1.06)], '395': [('459', 1.13), ('503', 1.17)], '396': [('355', 0.58), ('422', 1.08)], '488': [('531', 1.02), ('21', 0.53), ('505', 2.31), ('212', 1.27)], '303': [('499', 2.33), ('514', 1.34)], '398': [('155', 0.49), ('379', 1.29)], '399': [('141', 1.16), ('427', 1.21)], '400': [('380', 1.24), ('521', 1.02)], '247': [('451', 1.28), ('478', 1.2)], '401': [('402', 1.32), ('416', 1.29)], '22': [('437', 0.47), ('364', 0.2)], '373': [('356', 1.47), ('180', 1.3900000000000001)], '350': [('517', 1.19), ('481', 1.35)], '404': [('462', 1.17), ('507', 1.25)], '355': [('396', 1.04), ('319', 1.01)], '406': [('512', 1.5699999999999998), ('500', 1.47)], '11': [('517', 1.38)], '13': [('532', 0.37), ('530', 1.22)], '9': [('499', 2.29)], '278': [('277', 1.2), ('323', 1.26)], '187': [('454', 1.1), ('514', 1.1)], '111': [('239', 0.44), ('107', 1.11)], '376': [('221', 0.58), ('420', 1.06)], '386': [('335', 1.13), ('301', 1.26)], '409': [('313', 0.51), ('418', 0.36)], '328': [('196', 1.4), ('327', 1.5)], '410': [('354', 1.25), ('198', 1.19)], '402': [('401', 1.47), ('463', 1.07)], '261': [('267', 2.05), ('260', 1.31)], '299': [('319', 0.59), ('121', 2.3)], '378': [('233', 1.23), ('464', 1.13)], '520': [('502', 1.17), ('250', 1.19), ('214', 2.4), ('482', 2.09)], '338': [('489', 1.18), ('288', 1.37)], '359': [('480', 1.23), ('463', 1.52)], '414': [('413', 1.11), ('450', 1.1)], '383': [('144', 1.09), ('365', 1.19)], '307': [('166', 1.27), ('306', 1.31)], '500': [('406', 1.4), ('304', 1.56), ('253', 1.38), ('309', 1.11)], '492': [('501', 1.2), ('491', 1.18), ('17', 0.53)], '367': [('502', 1.29), ('333', 1.27)], '320': [('289', 1.22), ('134', 1.19)], '354': [('522', 1.47), ('410', 1.32)], '221': [('376', 0.56), ('131', 1.28)], '421': [('334', 1.1), ('264', 1.15)], '264': [('421', 1.11), ('468', 1.16)], '280': [('114', 1.03), ('341', 1.11)], '424': [('504', 1.52), ('507', 1.41)], '268': [('494', 1.3599999999999999), ('388', 0.48)], '285': [('168', 1.2), ('440', 1.16)], '532': [('533', 1.5899999999999999), ('113', 1.38), ('407', 1.12), ('505', 0.52), ('13', 0.36)], '324': [('455', 1.24), ('323', 1.29)], '179': [('513', 1.07), ('394', 1.18)], '8': [('96', 3.36)], '239': [('111', 0.4), ('217', 0.4)], '382': [('512', 1.32), ('501', 1.25)], '394': [('493', 1.1400000000000001), ('179', 1.19)], '310': [('462', 1.22), ('476', 0.55)], '368': [('433', 1.11), ('462', 1.23)], '255': [('254', 1.44), ('352', 1.29)], '331': [('425', 1.01), ('466', 1.03)], '343': [('504', 1.33), ('126', 1.4)], '139': [('468', 1.43), ('374', 1.04)], '363': [('512', 1.19), ('486', 1.48)], '249': [('248', 1.13), ('262', 1.1400000000000001)], '530': [('443', 1.2), ('533', 0.34), ('523', 0.57), ('533', 0.43)], '153': [('447', 1.37), ('474', 1.46)], '403': [('486', 1.34), ('529', 1.41)], '379': [('502', 1.28), ('398', 1.2)], '178': [('177', 1.37), ('385', 1.13)], '416': [('474', 1.3), ('401', 1.4)], '282': [('495', 1.07), ('281', 1.35)], '514': [('187', 1.2), ('342', 1.1400000000000001), ('366', 1.3900000000000001), ('303', 1.32)], '142': [('86', 0.57), ('470', 1.04)], '122': [('415', 1.16), ('348', 1.08)], '16': [('228', 1.1), ('88', 0.28)], '418': [('409', 0.35), ('430', 0.43)], '411': [('361', 1.11), ('316', 1.1400000000000001)], '336': [('318', 1.08), ('466', 1.34)], '24': [('528', 1.35), ('432', 0.35)], '510': [('141', 0.25), ('108', 1.2), ('84', 0.3)], '437': [('22', 0.44), ('536', 0.55), ('392', 0.47), ('525', 0.29)], '445': [('515', 0.31), ('442', 0.43), ('446', 1.07), ('528', 0.35)], '526': [('20', 1.25), ('523', 0.52), ('527', 0.53), ('523', 0.46), ('483', 0.57)], '527': [('526', 0.51), ('25', 1.25), ('526', 0.46), ('477', 0.57), ('518', 0.4)], '442': [('372', 0.25), ('445', 0.34), ('428', 0.36), ('508', 0.51)], '443': [('461', 1.11), ('530', 0.53), ('452', 1.02)], '25': [('527', 1.28), ('6', 0.35), ('528', 0.56)], '6': [('515', 0.4)], '0': None}'''


aStarAlgo('94', '162')


# duration of route in min
import connection as con

def get_route_duration(path):
    data = test.get_edges_predicted_duration_new('28 Mr 00_09_46')
    ls = path
    summe = 0
    for i in range(len(ls)-1):
        dic = con.get_connection(ls[i], ls[i + 1])
        num = dic.get("number")
        dura = data[int(num)]
        summe += dura
    return summe


print(get_route_duration(aStarAlgo('94', '162')))
