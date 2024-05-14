from collections import deque
from typing import Dict
import numpy as np
from Graph_directed import Graph, Vertex, Edge

    
def bfs(g : Graph, s :"Vertex", e : "Vertex"):
  visited = set([s])
  parent = {}
  q = deque([s])
  while q:
    node = q.popleft()
    for neighbour, edge in g.neighbours(node):
      e = edge
      if neighbour in visited or e.residualFlow <= 0:
        continue
      visited.add(neighbour)
      parent[neighbour] = node
      q.append(neighbour)
  return parent

def getMinFlow(g : "Graph", parent : Dict,s :"Vertex", t :"Vertex"):
  "funkcja oblicza minimalny przepływ w ścieżce"
  currNode = t
  minResidualFlow = np.inf
  if currNode not in parent.keys():
    return 0
  
  while currNode != s:
    e = g.getEdge(parent[currNode], currNode)
    if e.residualFlow < minResidualFlow:
      minResidualFlow = e.residualFlow
    currNode = parent[currNode]
  return minResidualFlow
  
def pathAugmentation(g, parent, minFlow, s, t):
  "funkcja redukująca przepływ w ścieżce"
  currNode = t
  
  while currNode != s:
    e = g.getEdge(parent[currNode], currNode)
    # if e.isResidual:
    #   er = e
    #   e = g.getEdge(currNode, parent[currNode])
    #   er.residualFlow -= minFlow
    #   e.residualFlow += minFlow
    #   e.flow -= minFlow
    # else:
    #   er = g.getEdge(currNode, parent[currNode])
    #   e.residualFlow -= minFlow
    #   e.flow += minFlow
    #   er.residualFlow += minFlow
    opposite = g.getEdge(currNode, parent[currNode])
    e.residualFlow -= minFlow
    opposite.residualFlow += minFlow
    if not e.isResidual:
      e.flow += minFlow
    else:
      opposite.flow -= minFlow 
      
    currNode = parent[currNode]
  return g

def sumFlow(g :"Graph", t:"Vertex"):
  sumF = 0
  for v1, v2, edge in g:
    if v1 == t or v2 == t:
      sumF += edge.flow
  return sumF 
  
def fordFulkerson(g : "Graph", s : "Vertex", t : "Vertex"):
  parent = bfs(g, s, t)
  minFlow = getMinFlow(g, parent, s, t)
  while minFlow > 0:
    g = pathAugmentation(g, parent, minFlow, s, t)
    parent = bfs(g, s, t)
    minFlow = getMinFlow(g, parent, s, t)

  return sumFlow(g,t)

def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")
    
    
def main():
  graphs = [[ ('s','u',2), ('u','t',1), ('u','v',3), ('s','v',1), ('v','t',2)],
            [ ('s', 'a', 16), ('s', 'c', 13), ('c', 'a', 4), ('a', 'b', 12), ('b', 'c', 9), ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4) ],
            [ ('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6), ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]]
  
  for graph in graphs:
    g = Graph()
    for edge in graph:
      e = Edge(edge[2])
      er = Edge(edge[2], True)
      v1 = Vertex(edge[0])
      v2 = Vertex(edge[1])
      g.insert_edge(v1, v2, e)
      g.insert_edge(v2, v1,er)
    # printGraph(g)
    start = g.get_vertex('s')
    end = g.get_vertex('t')
    print(fordFulkerson(g, start, end))
    printGraph(g)
        
if __name__ == '__main__':
  main()