#Uses python3

import sys
import queue

def bipartite(adj):
    colors = [None for _ in adj]
    for v in range(len(adj)):
        if colors[v] is None:
            bfs(adj, v, colors) 
    
    is_bipartite = 1
    for u, n in enumerate(adj):
        for v in n:
            if colors[u] == colors[v]:
                is_bipartite = 0
                break
    
    return is_bipartite

def get_opposite_color(color):
    if color == 1:
        return 0
    if color == 0:
        return 1

def bfs(adj, s, colors):
    colors[s] = 0
    Q = queue.Queue()
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for v in adj[u]:
                if colors[v] is None:
                    Q.put(v)
                    colors[v] = get_opposite_color(colors[u])               

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
