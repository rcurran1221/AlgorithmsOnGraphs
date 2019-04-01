#Uses python3

import sys

verticesCount = 0
adj = []
visited = []
pre = []
post = []
clock  = 0
edgesZero = []

def acyclic():
    for vertex in range(verticesCount):
        if not visited[vertex]:
            explore(vertex)
        
    is_acyclic = True
    for i, edge in enumerate(edgesZero):
        if post[edge[0]] < post[edge[1]]:
            is_acyclic = False
            
    return 0 if is_acyclic else 1

def explore(v):
    visited[v] = True
    previsit(v)
    for i, vertex in enumerate(adj[v]):
        if not visited[vertex]:
            explore(vertex)
    postvisit(v)

def previsit(v):
    global clock
    pre[v] = clock
    clock += 1
    
def postvisit(v):
    global clock
    post[v] = clock
    clock += 1

def arrange_inputs(data):
    global verticesCount
    global adj
    global visited
    global clock
    global pre
    global post
    global edgesZero
    
    n, m = data[0:2]
    verticesCount = n
    clock = 0
    visited = [False for _ in range(verticesCount)]
    pre = [0 for _ in range(verticesCount)]
    post = [0 for _ in range(verticesCount)]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    edgesZero = []
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        edgesZero.append([a-1, b-1])
        
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    arrange_inputs(data)
    print(acyclic())
