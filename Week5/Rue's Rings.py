for datasets in range(10):
    routes = int(input)
    diameters_lst = []
    min_diam = 70000

    for j in range(routes):
        row = input().split()
        for i in range(len(row)):
            row[i] = int(row[i])

        route_ID = row[0]
        diams = row[2:]
        current_diam = min(diams)

        if current_diam < min_diam:
            min_diam = current_diam
            diameters_lst = [route_ID]

        elif current_diam == min_diam:
            diameters_lst.append(route_ID)

        diameters_lst.sort()

        # figure out printing

