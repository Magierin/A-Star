import A_star_euclidean_distance as star
import quantity as quan
import connection as con
import test


def similar(ls_0, hour):
    counter = 0
    summe = 0
    for route in test.get_timestamp_route_list(hour):
        dup = [x for x in ls_0 if x in route]
        summe += len(dup)/len(ls_0)
        if len(dup)/len(ls_0) >= 0.75:
            counter += 1
    return counter/len(test.get_timestamp_route_list(hour))


def get_timestamp_route_list(timestamp):
    ts = timestamp.split()
    hour = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17'
            '18', '19', '20', '21', '22', '23']

    ls = []
    for i in hour:
        if ts[2].startswith(i):
            ls = quan.get_routes_quantity_per_hour()[hour.index(i)]
            break

    return ls


def get_edges_quan_per_hour_per(timestamp):
    routes = get_timestamp_route_list(timestamp)
    edges = []
    counter = []

    for i in range(len(routes)):
        for j in range(1, len(routes[i])):
            dic = con.get_connection(routes[i][j - 1], routes[i][j])
            num = dic.get('number')
            edges.append(int(num))

    for i in range(1308):
        c = edges.count(i)
        per = c / len(routes)
        counter.append(round(per, 4))

    return counter


def get_seventy_five_percent_similarity_percent():
    # per = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0037, 0.0037, 0.0077, 0.0077, 0.0077, 0.0077, 0.0077, 0.023, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0237, 0.0237, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0002, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0042, 0.0042, 0.0042, 0.0042, 0.0042, 0.0042, 0.0042, 0.027, 0.0506, 0.0, 0.0, 0.0, 0.0002, 0.0408, 0.0, 0.2908, 0.0, 0.0506, 0.0438, 0.0, 0.0173, 0.0, 0.0, 0.0, 0.0527, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0237, 0.0, 0.0, 0.0002, 0.0, 0.0007, 0.0019, 0.0, 0.0, 0.0656, 0.0, 0.0, 0.0, 0.0, 0.0005, 0.0005, 0.0, 0.0, 0.0, 0.003, 0.003, 0.0, 0.0, 0.0949, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0007, 0.0007, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0649, 0.1289, 0.1289, 0.1537, 0.1537, 0.1537, 0.0206, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0042, 0.063, 0.0007, 0.0, 0.0014, 0.0007, 0.0, 0.0, 0.0007, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0005, 0.0005, 0.0, 0.0, 0.0, 0.0602, 0.0, 0.0148, 0.0551, 0.0, 0.0846, 0.0, 0.0, 0.0905, 0.0202, 0.0084, 0.2105, 0.0, 0.0, 0.0, 0.0452, 0.0, 0.0, 0.0, 0.0028, 0.0, 0.4654, 0.0, 0.0122, 0.0, 0.0005, 0.1455, 0.0, 0.0, 0.0, 0.0059, 0.0, 0.0, 0.0, 0.0, 0.011, 0.0277, 0.1455, 0.0, 0.0, 0.0935, 0.0368, 0.0, 0.0098, 0.0262, 0.0452, 0.6285, 0.0, 0.0, 0.0002, 0.0, 0.0028, 0.0091, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0874, 0.0, 0.3131, 0.0, 0.6285, 0.0206, 0.027, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0098, 0.0014, 0.0005, 0.0, 0.2147, 0.0028, 0.0007, 0.0, 0.0237, 0.2641, 0.1411, 0.0, 0.0989, 0.0, 0.0009, 0.0227, 0.0, 0.0, 0.0696, 0.0098, 0.0, 0.0014, 0.0, 0.0, 0.0, 1.0, 0.0007, 0.0293, 0.0026, 0.4617, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.023, 0.0007, 0.0, 0.0026, 0.0, 0.0, 0.0002, 0.0129, 0.8378, 0.0, 0.011, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0091, 0.0642, 0.0, 0.0, 0.0, 0.0, 0.0077, 0.2641, 0.3122, 0.6691, 0.0, 0.0, 0.0045, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0084, 0.0293, 0.0002, 0.0, 0.0, 0.0, 0.0, 0.0457, 0.0293, 0.0, 0.0, 0.0262, 0.0, 0.0, 0.0, 0.0, 0.0352, 0.0014, 0.0084, 0.0005, 0.0516, 0.0098, 0.0757, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0098, 0.0, 0.1111, 0.0019, 0.0295, 0.0, 0.0028, 0.4654, 0.0112, 0.0312, 0.0, 0.0, 0.0012, 0.2112, 0.0, 0.2112, 0.6285, 0.0, 0.0, 0.0005, 0.0905, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0098, 0.0, 0.0, 0.0, 0.0, 0.7345, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0553, 0.6285, 0.0, 0.0, 0.0, 0.0183, 0.0005, 0.0183, 0.0197, 0.0277, 0.0, 0.011, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0696, 0.1455, 0.1029, 0.0026, 0.0, 0.0042, 0.0012, 0.1155, 0.0, 0.0, 0.0, 0.0335, 0.011, 0.0, 0.0, 0.6285, 0.2105, 0.0281, 0.0, 0.0, 0.0905, 0.0, 0.0, 0.0, 0.0183, 0.0, 0.0262, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0708, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.7345, 0.0, 0.2105, 0.0262, 0.1008, 0.8378, 0.0084, 0.0288, 0.0002, 0.0042, 0.023, 0.0, 0.0103, 0.0, 0.0, 0.0227, 0.0, 0.0, 0.0, 0.0005, 0.0288, 0.0337, 0.0007, 0.0, 0.0, 0.0197, 0.0042, 0.0028, 0.0, 0.0, 0.0, 0.0028, 0.0, 0.0, 0.0, 0.1029, 0.0, 0.1174, 0.8378, 0.0026, 0.0166, 0.0129, 0.0, 0.0923, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.6285, 0.0, 0.0042, 0.0, 0.0, 0.0028, 0.003, 0.0, 0.0103, 0.0, 0.0, 0.0, 0.1411, 0.0007, 0.0, 0.0042, 0.0, 0.0, 0.0295, 0.0162, 0.0375, 0.0, 0.0096, 0.0, 0.8378, 0.0206, 0.0, 0.0, 0.0, 0.1455, 0.0, 0.0, 0.0, 0.0506, 0.0, 0.0, 0.0258, 0.0002, 0.0045, 0.0, 0.0293, 0.0905, 0.0, 0.0077, 0.0, 0.0197, 0.0, 0.0197, 0.0, 0.0162, 0.0178, 0.0173, 0.0014, 0.0042, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0009, 0.0, 0.0, 0.0, 0.3122, 0.0, 0.0009, 0.0, 0.0, 0.0002, 0.0408, 0.0, 0.0, 0.153, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0227, 0.0, 0.3131, 0.0178, 0.2641, 0.0, 0.0977, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0696, 0.0452, 0.0, 0.0, 0.0005, 0.0, 0.0, 0.0, 0.018, 0.0012, 0.0, 0.0, 0.0, 0.0, 0.0, 0.6285, 0.0, 0.0173, 0.0506, 0.0, 0.0, 0.0, 0.0002, 0.0, 0.0, 0.0, 0.0, 0.0047, 0.0293, 0.0005, 0.3122, 0.0, 0.0, 0.0, 0.0005, 0.0, 0.0, 0.0, 0.0, 0.0047, 0.2641, 0.2105, 0.0028, 0.0, 0.0, 0.0007, 0.0009, 0.0209, 0.0, 0.0935, 0.0, 0.0, 0.0033, 0.2641, 0.0, 0.0134, 0.0, 0.0, 0.0, 0.0042, 0.0005, 0.0197, 0.0068, 0.153, 0.0, 0.1036, 0.0, 0.0014, 0.0551, 0.2105, 0.0, 0.6285, 0.0002, 0.0, 0.1111, 0.0, 0.0, 0.0002, 0.0206, 0.0211, 0.0091, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0368, 0.0211, 0.0, 0.3436, 0.0, 0.0977, 0.2112, 0.0, 0.0002, 0.0084, 0.0063, 0.0, 0.1158, 0.0295, 0.0002, 0.0, 0.0, 0.2339, 0.0, 0.0, 0.0, 0.0, 0.2112, 0.0183, 0.0, 0.0457, 0.0, 0.0, 0.0, 0.0, 0.0206, 0.0002, 0.0178, 0.0014, 0.0005, 0.0, 0.0675, 0.0, 0.0, 0.0, 0.0166, 0.0, 0.0419, 0.0005, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0935, 0.011, 0.0007, 0.0, 0.0209, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4143, 0.0424, 0.0012, 0.0696, 0.0, 0.0211, 0.0, 0.0, 0.0, 0.0084, 0.0, 0.0016, 0.0, 0.6285, 0.0, 0.0, 0.0, 0.0, 0.0094, 0.0, 0.0, 0.0, 0.0, 0.0134, 0.0, 0.0, 0.0, 0.0, 0.0, 0.8378, 0.0, 0.1465, 0.0, 0.0007, 0.0, 0.0, 0.0, 0.1411, 0.0, 0.0237, 0.0, 0.0, 0.0, 0.6285, 0.0, 0.0, 0.0, 0.0, 0.0262, 0.0237, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2105, 0.0, 0.0, 0.0457, 0.0091, 0.0, 0.0, 0.0, 0.6285, 0.0098, 0.0, 0.153, 0.0, 0.0, 0.0, 0.138, 0.0, 0.3478, 0.2775, 0.0, 0.0, 0.0, 0.0, 0.0162, 0.101, 0.0, 0.0, 0.0026, 0.0, 0.0007, 0.0, 0.0007, 0.0424, 0.0, 0.0, 0.0005, 0.0, 0.0258, 0.0, 0.0007, 0.0, 0.0042, 0.0002, 0.0, 0.0, 0.0042, 0.0, 0.0, 0.1336, 0.0087, 0.0905, 0.0, 0.0012, 0.0, 0.0, 0.0002, 0.0, 0.0026, 0.0, 0.0002, 0.0094, 0.0129, 0.0, 0.0, 0.0492, 0.0103, 0.0002, 0.0087, 0.0197, 0.0, 0.0, 0.0, 0.0012, 0.0, 0.0007, 0.0, 0.0002, 0.0, 0.0675, 0.0002, 0.0783, 0.0202, 0.0, 0.0012, 0.0, 0.0, 0.0237, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0281, 0.3131, 0.0, 0.0014, 0.0, 0.2147, 0.0077, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0319, 0.0, 0.0, 0.0279, 0.3827, 0.0, 0.4617, 0.0, 0.0, 0.0, 0.0005, 0.0891, 0.0, 0.0345, 0.0, 0.0134, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0349, 0.0757, 0.0183, 0.0143, 0.0, 0.0, 0.034, 0.0279, 0.0014, 0.0, 0.7345, 0.0, 0.0, 0.0, 0.0103, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0098, 0.0, 0.6285, 0.0, 0.0084, 0.0, 0.0492, 0.0007, 0.0178, 0.0, 0.0, 0.0, 0.1411, 0.0, 0.0103, 0.0007, 0.0, 0.0028, 0.0, 0.0, 0.2641, 0.0007, 0.0, 0.0607, 0.0, 0.0014, 0.0, 0.0, 0.0, 0.0246, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0173, 0.0033, 0.0, 0.0977, 0.0, 0.0, 0.0, 0.1901, 0.0, 0.0, 0.1174, 0.0, 0.6285, 0.0, 0.0, 0.0, 0.0026, 0.0921, 0.0534, 0.0419, 0.0, 0.0, 0.0293, 0.0, 0.0005, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0237, 0.0696, 0.0, 0.0248, 0.0, 0.0, 0.0042, 0.0, 0.0, 0.0012, 0.0, 0.0, 0.0005, 0.0424, 0.0002, 0.0935, 0.0, 0.0607, 0.0002, 0.0, 0.0206, 0.0197, 0.0, 0.0277, 0.0206, 0.0, 0.0, 0.0084, 0.0002, 0.0, 0.0, 0.0103, 0.0045, 0.0, 0.0, 0.0, 0.0, 0.153, 0.0, 0.0, 0.0, 0.0007, 0.0, 0.0312, 0.0183, 0.0143, 0.0, 0.0, 0.0352, 0.0096, 0.0, 0.0295, 0.0, 0.0237, 0.0, 0.8378, 0.0, 0.3715, 0.0, 0.0, 0.0129, 0.0933, 0.0, 0.0007, 0.0, 0.0237, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.6285, 0.0, 0.0002, 0.0014, 0.0, 0.0, 0.1411, 0.0, 0.0668, 0.0, 0.0206, 0.0, 0.0134, 0.0, 0.0, 0.0, 0.0, 0.0424, 0.0, 0.0, 0.0, 0.0492, 0.153, 0.0, 0.1111, 0.0, 0.0, 0.0905, 0.0122, 0.0295, 0.0, 0.0016, 0.0, 0.0, 0.0492, 0.0002, 0.0, 0.0162, 0.0173, 0.0, 0.0701, 0.0, 0.0, 0.3827, 0.0, 0.1008, 0.0, 0.0, 0.0, 0.0457, 0.2147, 0.0, 0.0, 0.0, 0.0077, 0.0002, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0002, 0.0, 0.0368, 0.0, 0.0, 0.0, 0.4617, 0.0091, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0696, 0.0, 0.0, 0.0, 0.003, 0.0, 0.0, 0.0122, 0.0166, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0002, 0.2112, 0.0, 0.0, 0.0, 0.0783, 0.0, 0.3131, 0.0989, 0.3136, 0.0, 0.0012, 0.0009, 0.0, 0.0, 0.0, 0.0005, 0.0319, 0.0, 0.0, 0.0005, 0.0007, 0.109, 0.0002, 0.0, 0.0002, 0.0, 0.0045, 0.0005, 0.0, 0.0098, 0.0, 0.0037, 0.0298, 0.0, 0.0019, 0.0016, 0.0534, 0.1411, 0.0005, 0.2351, 0.3541, 0.0084, 0.0005, 0.0244, 0.0, 0.0801, 0.0, 0.0, 0.0984, 0.019, 0.0, 0.0042, 0.0, 0.3136, 0.3143, 0.0, 0.0007, 0.0, 0.0, 0.0002, 0.0014, 0.0045, 0.0, 0.0, 0.0, 0.0023, 0.0, 0.0511, 0.0, 0.1392, 0.0169, 0.0, 0.1162, 0.033, 0.0, 0.4617, 0.131, 0.0, 0.0, 0.0, 0.0157, 0.0, 0.3274, 0.0, 0.0497, 0.0005, 0.1577, 0.2775, 0.0002, 0.0, 0.0152, 0.0687, 0.0, 0.0]
    timestamp = test.get_timestamp_all()[4267:]
    paths = []
    for time in timestamp:
        per = get_edges_quan_per_hour_per(time)
        path = star.aStarAlgo(time, per)
        paths.append(similar(path, time))
        print(paths)
    return paths


print(get_seventy_five_percent_similarity_percent())
