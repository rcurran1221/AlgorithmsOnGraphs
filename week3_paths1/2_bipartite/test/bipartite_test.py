#Uses python3

import sys
import queue

def bipartite(adj):
    dist, colors = bfs(adj, 0)    
    
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

def bfs(adj, s):
    dist = [-1 for _ in adj]
    colors = [0 for _ in adj]
    dist[s] = 0
    Q = queue.Queue()
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for v in adj[u]:
                if dist[v] == -1:
                    Q.put(v)
                    dist[v] = dist[u] + 1
                    colors[v] = get_opposite_color(colors[u])
    return dist, colors

def is_bipartite(data):
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))

if __name__ == '__main__':
    caseOne = [4,4,
               1,2,
               4,1,
               2,3,
               3,1]
    is_bipartite(caseOne)
    
    caseTwo = [5,4,
               5,2,
               4,2,
               3,4,
               1,4]
    is_bipartite(caseTwo)