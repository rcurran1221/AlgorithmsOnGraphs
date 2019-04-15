#Uses python3

import sys
import queue


def distance(adj, cost, s, t):
    dist = [sys.maxsize for _ in range(len(adj))]
    prev = [None for _ in range(len(adj))]
    valid = [1 for _ in range(len(adj))]
    dist[s] = 0
    h = queue.PriorityQueue()
    for v, d in enumerate(dist):
        h.put((v, d))
    while h and all(i != 0 for i in valid):
        u, d = h.get()
        if valid[u] == 0:
            continue
        for i, v in enumerate(adj[u]):
            if dist[v] > dist[u] + cost[u][i]:
                dist[v] = dist[u] + cost[u][i]
                prev[v] = u
                valid[v] = 0
                h.put((v, dist[v]))
            
    return dist[t]

def compute_shortest_distance(data):
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    
    print(distance(adj, cost, s, t))
    
if __name__ == '__main__':
    caseOne = [4, 4,
               1,2,1,
               4,1,2,
               2,3,2,
               1,3,5,
               1,3]
    compute_shortest_distance(caseOne)