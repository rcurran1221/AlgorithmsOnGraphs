#Uses python3

#import sys

visited = []
adj = []
verticiesCount = 0

def reach(x, y):
    explore(x)    
    return 1 if visited[y] else 0

def explore(v):
    visited[v] = True
    for y in range(len(adj[v])):
        if not visited[adj[v][y]]:
            explore(adj[v][y])
    
def canExitMaze(data):
    global adj
    global verticiesCount
    global visited
    n, m = data[0:2]
    verticiesCount = n
    visited = [False for _ in range(verticiesCount)]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(x, y))

if __name__ == '__main__':
    caseOne = [4, 4,
               1, 2,
               3, 2,
               4, 3,
               1, 4,
               1, 4,]
    canExitMaze(caseOne)
    
    caseTwo = [4, 2,
               1, 2,
               3, 2,
               1, 4]
    canExitMaze(caseTwo)

    caseThree = [7, 5,
                 0, 2,
                 2, 3,
                 3, 4,
                 1, 5,
                 5, 6,
                 0, 5]
    canExitMaze(caseThree)
    
    caseFour =  [7, 5,
                 0, 2,
                 2, 3,
                 3, 4,
                 1, 5,
                 5, 6,
                 2, 4]
    canExitMaze(caseFour)
    
    
    