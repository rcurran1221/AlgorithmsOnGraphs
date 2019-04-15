#Uses python3

import sys
import queue


def distance(adj, cost, s, t):
    dist = [sys.maxsize for _ in range(len(adj))]
    prev = [None for _ in range(len(adj))]
    processed = [0 for _ in range(len(adj))]
    dist[s] = 0
    
    h = queue.PriorityQueue()
    for v, d in enumerate(dist):
        h.put((d, v))
        
    while not h.empty():
        d, u = h.get()
        if processed[u] == 1:
            continue
        
        processed[u] = 1
        for i, v in enumerate(adj[u]):
            if dist[v] > dist[u] + cost[u][i]:
                dist[v] = dist[u] + cost[u][i]
                prev[v] = u
                h.put((dist[v], v))
            
    return dist[t] if dist[t] != sys.maxsize else -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
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
