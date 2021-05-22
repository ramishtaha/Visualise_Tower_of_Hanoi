temp = []
towers = {
    'Source': [],
    'Destination': [],
    'Auxiliary': [],
}


def init_tower_a(n):
    global towers
    for i in range(1, n + 1):
        s = '█' + '█' * i * 2
        temp.append(s)
    towers['Source'] += temp[::-1]


def print_towers(n):
    t = towers["Source"][::-1]
    u = towers["Destination"][::-1]
    v = towers["Auxiliary"][::-1]
    p = len(t)
    q = len(u)
    r = len(v)
    ds = n - p
    dd = n - q
    da = n - r

    for j in range(n):
        a = j - ds
        if a >= 0:
            print(t[a].center(21), end="  ")
        else:
            print('║'.center(21), end="  ")
        b = j - dd
        if b >= 0:
            print(u[b].center(21), end="  ")
        else:
            print('║'.center(21), end="  ")
        c = j - da
        if c >= 0:
            print(v[c].center(21))
        else:
            print('║'.center(21))

    print('═════════════════════', end="  ")
    print('═════════════════════', end="  ")
    print('═════════════════════')
    print('Source'.center(21), end="  ")
    print('Destination'.center(21), end="  ")
    print('Auxiliary'.center(21))


def move(source, destination):
    global towers
    towers[destination].append(towers[source][-1])
    towers[source].pop(-1)
