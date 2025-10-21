from collections import deque
import math
from itertools import combinations

def read_input():
    number_of_rooms = int(input())
    rooms = [int(input()) for _ in range(number_of_rooms)]
    return rooms

def build_graph(rooms):
    """Build graph as adjacency dictionary with capacities"""
    graph = {}

    def add_edge(u, v, capacity):
        if u not in graph:
            graph[u] = {}
        if v not in graph:
            graph[v] = {}
        
        # Add forward edge with capacity
        graph[u][v] = capacity
        
        # Add backward edge with 0 capacity (for residual graph)
        if u not in graph[v]:
            graph[v][u] = 0

    # Initialize all rooms in the graph
    for room in rooms:
        if room not in graph:
            graph[room] = {}

    # Add edges based on GCD > 1 (both ways)
    for a, b in combinations(rooms, 2):
        g = math.gcd(a, b)
        if g > 1:
            add_edge(a, b, g)
            add_edge(b, a, g)

    return graph

def bfs(graph, source, sink, parent):
    """Find path from source to sink using BFS"""
    visited = set()
    queue = deque([source])
    visited.add(source)
    parent.clear()  # Clear parent dictionary

    while queue:
        u = queue.popleft()
        if u in graph:  # Check if node exists in graph
            for v, capacity in graph[u].items():
                if v not in visited and capacity > 0:
                    visited.add(v)
                    parent[v] = u
                    if v == sink:
                        return True
                    queue.append(v)
    return False

def edmonds_karp(graph, source, sink):
    """Compute maximum flow from source to sink"""
    max_flow = 0
    parent = {}

    # Check if source and sink exist
    if source not in graph or sink not in graph:
        return 0

    while bfs(graph, source, sink, parent):
        # Find bottleneck along path
        path_flow = float('inf')
        s = sink
        while s != source:
            if parent[s] not in graph or s not in graph[parent[s]]:
                path_flow = 0
                break
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        if path_flow == 0:
            break

        # Update residual capacities
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

        max_flow += path_flow

    return max_flow

if __name__ == "__main__":
    rooms = read_input()
    graph = build_graph(rooms)
    
    # Entrance is the lowest-numbered room, exit is the highest-numbered room
    entrance = min(rooms)
    exit = max(rooms)
    
    max_flow = edmonds_karp(graph, entrance, exit)
    print(max_flow)
