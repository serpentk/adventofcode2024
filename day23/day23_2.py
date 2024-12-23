import sys

def get_subgraph(graph, item):
    return {x: set.intersection(graph[item], graph[x]) for x in graph[item]}


def clique(graph):
    codes = {item: 2**i for i, item in enumerate(graph)}
    relations = codes.copy()
    res = set()
    for item in graph:
        for x in graph[item]:
            relations[item] += codes[x]
    for code in range(1, 2 ** len(graph)):
        if code.bit_count() <= len(res):
            continue
        members = [item for item in graph if code & relations[item] == code]
        if len(members) != code.bit_count():
            continue
        res = set(members)
    return res


network = dict()
for line in sys.stdin:
    x, y = line.strip().split('-')
    network.setdefault(x, set()).add(y)
    network.setdefault(y, set()).add(x)

password = ''
for item in network:
    cl = clique(get_subgraph(network, item))
    cur_pass = ','.join(sorted([item] + list(clique(get_subgraph(network, item)))))
    if len(cur_pass) > len(password):
        password = cur_pass
print(password, len(password))
