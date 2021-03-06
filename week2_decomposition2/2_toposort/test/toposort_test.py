#Uses python3

import sys

verticesCount = 0
adj = []
visited = []
pre = []
post = []
clock  = 0
edgesZero = []

def toposort():
    for vertex in range(verticesCount):
        if not visited[vertex]:
            explore(vertex)
    
    return [i[0] for i in sorted(enumerate(post), key=lambda x:x[1], reverse=True)]

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

def arrange_and_toposort(data):
    arrange_inputs(data)
    order = toposort()
    for x in order:
        print(x + 1, end=' ')

if __name__ == '__main__':
    caseOne = [4,3,
               1,2,
               4,1,
               3,1]
    expectedOne = [4,3,1,2]
    arrange_and_toposort(caseOne)
    
    caseTwo = [4,1,
               3,1]
    expectedTwo = [2,3,1,4]
    arrange_and_toposort(caseTwo)
    
    caseThree = [5,7,
                 2,1,
                 3,2,
                 3,1,
                 4,3,
                 4,1,
                 5,2,
                 5,3]
    expectedThree = [5,4,3,2,1]
    arrange_and_toposort(caseThree)

