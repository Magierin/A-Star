#https://www.mygreatlearning.com/blog/a-search-algorithm-in-artificial-intelligence/
import duration


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
Graph_nodes = dict()
p = pc.parse_csv()
counter = 0
liste = []
for i in range(len(p)-1):
    fro = p[i].get("from")
    if fro in liste:
        continue
    to = p[i].get("to")
    lst = []
    for j in range(counter, len(p)-1):
        if fro == p[j].get("from"):
            lst.append((str(p[j].get("to")), dis.get_edge_num_dist(j)))
            if fro not in liste:
                liste.append(fro)
    counter += 1
    Graph_nodes[str(fro)] = lst
Graph_nodes['0'] = None


aStarAlgo('94', '162')


# duration of route in min
import connection as con


def get_route_duration(path):
    data = duration.get_edges_predicted_duration()
    print(data)
    ls = path
    summe = 0
    for i in range(len(ls)-1):
        dic = con.get_connection(ls[i], ls[i + 1])
        num = dic.get("number")
        dura = data[int(num)]
        summe += dura
    return summe


print(get_route_duration(aStarAlgo('94', '162')))
