from graph import Vertex, Graph
import numpy as np
from graf_mst import graf

def prim(g: "Graph", s : "Vertex"):
  vertices = g.vertices()
  intree = {v : False for v in vertices}
  distance = {v : np.inf for v in vertices}
  parent = {v: None for v in vertices}
  mst = Graph()
  currentNode = s
  while not intree[currentNode]:
    intree[currentNode] = True
    for neighbour, weight in g.neighbours(currentNode):
      if intree[neighbour]:
        continue
      if weight < distance[neighbour]:
        parent[neighbour] = currentNode
        distance[neighbour] = weight
    
    intree[currentNode] = True
    if parent[currentNode]:
      mst.insert_edge(parent[currentNode], currentNode, distance[currentNode])
    minWeight = np.inf
    for node in vertices:
      if not intree[node] and distance[node] < minWeight:
        minWeight = distance[node]
        currentNode = node
  return mst, np.sum([w for _,_,w in mst.edges()])
        
    
def test(edges):
  g = Graph()
  for e1, e2, weight in edges:
    v1 = Vertex(e1)
    v2 = Vertex(e2)
    g.insert_edge(v1,v2,weight)
  mst, l = prim(g, g.vertices()[0])
  mst.printGraph()
  
  
def main():
  graf = [ ('A','B',4), ('A','C',1), ('A','D',4),
         ('B','E',9), ('B','F',9), ('B','G',7), ('B','C',5),
         ('C','G',9), ('C','D',3),
         ('D', 'G', 10), ('D', 'J', 18),
         ('E', 'I', 6), ('E', 'H', 4), ('E', 'F', 2),
         ('F', 'H', 2), ('F', 'G', 8),
         ('G', 'H', 9), ('G', 'J', 8),
         ('H', 'I', 3), ('H','J',9),
         ('I', 'J', 9)
        ]
  # edges = [
  #     ('A', 'B', 4),
  #     ('A', 'C', 1),
  #     ('A', 'D', 4),
  #     ('B', 'D', 4),
  #     ('B', 'G', 7),
  #     ('B', 'F', 2),
  #     ('C', 'D', 3),
  #     ('D', 'G', 10),
  #     ('E', 'F', 2),
  #     ('E', 'H', 4),
  #     ('E', 'I', 3),
  #     ('F', 'G', 8),
  #     ('F', 'H', 9),
  #     ('G', 'J', 8),
  #     ('H', 'J', 9),
  #     ('I', 'J', 9)
  # ]
  test(graf)
  
if __name__ == "__main__":
  main()
