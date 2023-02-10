buildings,routes = [int(x) for x in input().split()]
connections_map = {}
for x in range(routes):
    start,end = [int(x) for x in input().split()]
    if end in connections_map:
        connections_map[end].add(start)
    else:
        connections_map[end] = set({start})

num_connections = 0
ans = []

for x in range(buildings):
    temp_conn = {x}
    if x in connections_map:
        connected_buildings = connections_map[x]
        temp_conn = temp_conn.union(connected_buildings)

        for y in connected_buildings:
            if y in connections_map:
                temp_conn = temp_conn.union(connections_map[y])

    if len(temp_conn) > num_connections:
        num_connections = len(temp_conn)
        ans.clear()
    if len(temp_conn) == num_connections:
        ans.append(str(x))

print(num_connections)
ans = " ".join(ans)
print(ans)