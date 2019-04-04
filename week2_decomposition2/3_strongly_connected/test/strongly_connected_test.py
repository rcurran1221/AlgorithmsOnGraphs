#Uses python3

import sys

sys.setrecursionlimit(200000)

verticesCount = 0
clock  = 0
deleted = []

def number_of_strongly_connected_components(adj, edgesZero, visited, post):
    global clock
    scc = 0    
    adjR = reverse_graph(edgesZero, adj)
    
    while not all(i == 1 for i in deleted):    
        clock = 0
        dfs(adjR, visited, post)        
        v = get_largest_post(post)
        visited = [False for i in range(verticesCount)]
        explore(v, adjR, post, visited)
        
        verticesToDelete = []
        for vertex, wasVisited in enumerate(visited):
            if wasVisited and is_active(vertex):
                verticesToDelete.append(vertex)
        
        for vertex in verticesToDelete:
            deleted[vertex] = 1
        
        scc += 1
        
        post = [0 for i in range(verticesCount)]
        visited = [False for i in range(verticesCount)]
    
    return scc

def get_largest_post(post):
    v = 0
    for i, postTime in enumerate(post):
        if is_active(i) and postTime > post[v]:
            v = i
    return v

def is_active(vertex):
    return deleted[vertex] == 0

def reverse_graph(edgesZero, adj):
    adjR = [[] for i in range(verticesCount)]
    edgesZeroR = [[] for i in range(len(edgesZero))]
    for i, edge in enumerate(edgesZero):
        edgesZeroR[i].append(edge[1])
        edgesZeroR[i].append(edge[0])
        if is_active(edge[1]) and is_active(edge[0]):
            adjR[edge[1]].append(edge[0])
    
    return adjR

def dfs(adj, visited, post):
    for vertex in range(len(visited)):
        if not visited[vertex]:
            explore(vertex, adj, post, visited)

def explore(v, adj, post, visited):
    if not is_active(v):
        return
    previsit(v)
    visited[v] = True
    for vertex in adj[v]:
        if not visited[vertex]:
            explore(vertex, adj, post, visited)
    postvisit(v, post)

def previsit(v):
    global clock
    if not is_active(v):
        return
    clock += 1

def postvisit(v, post):
    global clock
    if not is_active(v):
        return
    post[v] = clock
    clock += 1

def arrange_inputs(data):
    global clock
    global deleted
    global verticesCount
    
    n, m = data[0:2]
    verticesCount = n
    clock = 0
    visited = [False for _ in range(verticesCount)]
    post = [0 for _ in range(verticesCount)]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(verticesCount)]
    deleted = [0 for _ in range(verticesCount)]
    edgesZero = []
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        edgesZero.append([a-1, b-1])
    return adj, edgesZero, visited, post

def arrange_and_print(data):
    adj, edgesZero, visited, post = arrange_inputs(data)
    scc = number_of_strongly_connected_components(adj, edgesZero, visited, post)
    print(scc)

if __name__ == '__main__':
    caseOne = [4, 4,
               1, 2,
               4, 1,
               2, 3,
               3, 1]
    arrange_and_print(caseOne)
    
    caseTwo = [5,7,
               2,1,
               3,2,
               3,1,
               4,3,
               4,1,
               5,2,
               5,3]
    
    arrange_and_print(caseTwo)
