#Uses python3

import sys


def negative_cycle(adj, cost):
    dist = [sys.maxsize for _ in range(len(adj))]
    prev = [None for _ in range(len(adj))]
    
    dist[0] = 0
    
    for _ in range(len(adj)-1):
        for u, a in enumerate(adj):
            for i, v in enumerate(a):
                if dist[v] > dist[u] + cost[u][i]:
                    dist[v] = dist[u] + cost[u][i]
                    prev[v] = u
    
    for u, a in enumerate(adj):
            for i, v in enumerate(a):
                if dist[v] > dist[u] + cost[u][i]:
                    return 1
    
    return 0

def test(data):
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))

if __name__ == '__main__':
    caseOne = [4,4,
               1,2,-5,
               4,1,2,
               2,3,2,
               3,1,1]
    test(caseOne)
    
    caseTwo = [5,4,
               1,2,1,
               3,4,-5,
               4,5,1,
               5,3,1]
    test(caseTwo)
    
    caseThree = [5,4,
               1,2,1,
               3,4,1,
               4,5,1,
               5,3,1]
    test(caseThree)
#    
    caseFour = [8,7,
               1,2,1,
               3,4,1,
               4,5,1,
               5,3,1,
               6,7,1,
               7,8,1,
               8,6,-10]
    test(caseFour)
