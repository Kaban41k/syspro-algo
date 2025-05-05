def kosaraju(graph):
    graph_rev = {}
    nodes = []
    mask = {}

    arr = []

    for node in graph.keys():
        nodes.append(node)
        mask[node] = False
        for next_node in graph[node]:
            if next_node not in graph.keys():
                mask[next_node] = False
                nodes.append(next_node)

    for node in graph.keys():
        for next_node in graph[node]:
            if next_node not in graph_rev.keys():
                graph_rev[next_node] = [node]
            else:
                graph_rev[next_node].append(node)

    arr = []

    def dfs(node):
        mask[node] = True
        if node in graph_rev.keys():
            for next in graph_rev[node]:
                if not mask[next]:
                    dfs(next)
        arr.append(node)

    n = len(nodes)

    for i in range(n):
        if not mask[nodes[i]]:
            dfs(nodes[i])

    arr.reverse()
    for key in mask.keys():
        mask[key] = False

    def dfs2(node, way):
        mask[node] = True
        if node in graph.keys():
            for next in graph[node]:
                if not mask[next]:
                    dfs2(next, way)
        way.append(node)

    scc = []

    for node in arr:
        if not mask[node]:
            way = []
            dfs2(node, way)
            scc.append(way)
    return scc


def solve(funcs):
    sccs = kosaraju(funcs)

    for scc in sccs:
        if len(scc) != 1:
            for node in scc:
                print(node, "rec")
        else:
            if scc[0] in funcs.keys() and scc[0] in funcs[scc[0]]:
                print(scc[0], "rec")
            else:
                print(scc[0], "not rec")
    print(sccs)

    return max(list(map(len, sccs)))


tests = [{"foo": ["bar", "baz", "qux"],
          "bar": ["baz", "foo", "bar"],
          "qux": ["qux"]},

         {1: [1],
          4: [1, 2, 3]},

         {1: [1, 4],
          4: [1, 2, 3]},

         {1: [1, 2, 3, 4, 5]}]

for test in tests:
    print("ANSWER:", solve(test))
    print("-" * 40)
