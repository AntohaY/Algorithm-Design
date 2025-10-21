from collections import deque, defaultdict

def read_input():
    n, m, k = map(int, input().split())

    children_likes = []
    for _ in range(n):
        parts = list(map(int, input().split()))
        count = parts[0]
        toys = parts[1:1 + count]
        children_likes.append(toys)

    categories = []
    for _ in range(k):
        parts = list(map(int, input().split()))
        count = parts[0]
        toys = parts[1:1 + count]
        limit = parts[-1]
        categories.append({"toys": toys, "limit": limit})

    return n, m, k, children_likes, categories

def build_graph(n, m, k, children_likes, categories):
    graph = defaultdict(dict)
    source = "S"
    sink = "T"

    # Source -> Children
    for i in range(n):
        graph[source][f"C{i}"] = 1

    # Children -> Toys
    for i, toys in enumerate(children_likes):
        for toy in toys:
            graph[f"C{i}"][f"T{toy}"] = 1

    # Toys -> Categories (or directly to sink if no category)
    toy_to_category = {}
    for c_idx, cat in enumerate(categories):
        for toy in cat["toys"]:
            toy_to_category[toy] = f"G{c_idx}"

    for toy in range(1, m+1):
        toy_node = f"T{toy}"
        if toy in toy_to_category:
            graph[toy_node][toy_to_category[toy]] = 1
        else:
            # toy without category goes straight to sink
            graph[toy_node][sink] = 1

    # Categories -> Sink
    for i, cat in enumerate(categories):
        graph[f"G{i}"][sink] = cat["limit"]

    return graph, source, sink

def bfs(graph, source, sink, parent):
    visited = set([source])
    q = deque([source])
    while q:
        u = q.popleft()
        for v, cap in graph[u].items():
            if v not in visited and cap > 0:
                visited.add(v)
                parent[v] = u
                if v == sink:
                    return True
                q.append(v)
    return False

def edmonds_karp(graph, source, sink):
    max_flow = 0
    while True:
        parent = {}
        if not bfs(graph, source, sink, parent):
            break
        # find minimum residual capacity on the path
        path_flow = float('inf')
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, graph[u][v])
            v = u
        # update residual capacities
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v].setdefault(u, 0)
            graph[v][u] += path_flow
            v = u
        max_flow += path_flow
    return max_flow

if __name__ == "__main__":
    n, m, k, children_likes, categories = read_input()
    graph, source, sink = build_graph(n, m, k, children_likes, categories)
    max_flow = edmonds_karp(graph, source, sink)
    print(max_flow)
