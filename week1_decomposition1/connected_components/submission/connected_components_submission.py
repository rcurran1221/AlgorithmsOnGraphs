#Uses python3

import sys

adj = []
verticiesCount = 0
visited = []
connectedComponent = 0

def number_of_components():
    global connectedComponent
    for vertex in range(verticiesCount):
        if not visited[vertex]:
            explore(vertex)
            connectedComponent += 1
    return connectedComponent

def explore(v):
    visited[v] = True
    for i, vertex in enumerate(adj[v]):
        if not visited[vertex]:
            explore(vertex)

def arrange_inputs(data):
    global verticiesCount
    global adj
    global visited
    global connectedComponent
    n, m = data[0:2]
    verticiesCount = n
    visited = [False for _ in range(verticiesCount)]
    connectedComponent = 0
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
        
def calculate_number_of_components(data):
    arrange_inputs(data)
    print(number_of_components())

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    calculate_number_of_components(data)
