#Uses python3
import sys
import math

def minimum_distance(x, y):
    edgesSorted = sorted(generate_edges(x, y), key = lambda edge : edge[2])
    setCollection = []
    for i in range(len(x)):
        setCollection.append({i})
    
    minSpanTree = []
    
    for edge in edgesSorted:
        setIndexA = find(setCollection, edge[0])
        setIndexB = find(setCollection, edge[1])
        if setIndexA != setIndexB:
            minSpanTree.append(edge)
            union(setIndexA, setIndexB, setCollection)
            
    return calculate_msp_weight(minSpanTree)

def calculate_msp_weight(minSpanTree):
    result = 0.
    
    for edge in minSpanTree:
        result += edge[2]
    
    return result

def find(setCollection, vertex):
    for i, s in enumerate(setCollection):
        if s is not None and vertex in s:
            return i

def union(setIndexA, setIndexB, setCollection):
    setA = setCollection[setIndexA]
    setB = setCollection[setIndexB]
    
    union = setA.union(setB)
    
    setCollection[setIndexA] = None
    setCollection[setIndexB] = None
    setCollection.append(union)

def generate_edges(x, y):
    edgeExists = {}
    
    edges = []
    for i in range(len(x)):
        for z in range(len(x)):
            if i == z:
                continue
            if (i,z) in edgeExists:
                continue
            edgeLength = calculate_edge_length((x[i], y[i]), (x[z], y[z]))
            edges.append((i, z, edgeLength))
            edgeExists[(i,z)] = True
            edgeExists[(z,i)] = True
            
    return edges

def calculate_edge_length(pointA, pointB):
    xDist2 = (pointA[0] - pointB[0])**2
    yDist2 = (pointA[1] - pointB[1])**2
    
    return math.sqrt(xDist2 + yDist2)   

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
