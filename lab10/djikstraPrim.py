from graph import Vertex, Graph
import numpy as np

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
      mst.insert_edge(currentNode, parent[currentNode], distance[currentNode])
    minWeight = np.inf
    for node in vertices:
      if not intree[node] and distance[node] < minWeight:
        minWeight = distance[node]
        currentNode = node
  return mst, np.sum([w for _,_,w in mst.edges()])
        
    
def main():
  edges = [
      ('A', 'B', 4),
      ('A', 'C', 1),
      ('A', 'D', 3),
      ('B', 'D', 4),
      ('B', 'G', 7),
      ('B', 'F', 2),
      ('C', 'D', 1),
      ('D', 'G', 10),
      ('E', 'F', 2),
      ('E', 'H', 4),
      ('E', 'I', 3),
      ('F', 'G', 8),
      ('F', 'H', 9),
      ('G', 'J', 8),
      ('H', 'I', 9),
      ('I', 'J', 9)
  ]
  g = Graph()
  for e1, e2, weight in edges:
    v1 = Vertex(e1)
    v2 = Vertex(e2)
    g.insert_edge(v1,v2,weight)
  mst, l = prim(g, g.vertices()[0])
  print(l)
if __name__ == "__main__":
  main()
