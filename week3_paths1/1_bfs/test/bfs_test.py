#Uses python3

import sys
import queue

def distance(adj, s, t):
    dist = bfs(adj, s)
    return dist[t]

def bfs(adj, s):
    dist = [-1 for _ in adj]
    dist[s] = 0
    Q = queue.Queue()
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for v in adj[u]:
                if dist[v] == -1:
                    Q.put(v)
                    dist[v] = dist[u] + 1
    return dist

def find_min_distance(data):
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))

if __name__ == '__main__':
    caseOne = [4,4,
               1,2,
               4,1,
               2,3,
               3,1,
               2,4]
    find_min_distance(caseOne)
    
    caseTwo = [5,4,
               5,2,
               1,3,
               3,4,
               1,4,
               3,5]
    find_min_distance(caseTwo)
