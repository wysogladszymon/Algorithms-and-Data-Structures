from Graph_dependency import Graph, Vertex
# from Graph_matrix import Graph, Vertex
from collections import deque
import polska

def coloringBFS(g : Graph):
  v= g.vertices()
  start = v[0]
  q = deque([start])
  visited = set()
  color = {x : -1 for x in g.vertices()}
  n = len(g.vertices())
  while q:
    node = q.popleft()
    visited.add(node)
    
    taken = [False] * n
    for neighbour in g.neighbours(g.get_vertex()):
      if neighbour not in visited:
        q.append(neighbour)
        continue
      taken[color[neighbour]] = True
      
    for index, w in enumerate(taken):
      if not w:
        color[node] = index
        break
    
  return color
        
        

def main():
  data = polska.graf
  g = Graph()
  
  for tup in data:
    v1 = Vertex(tup[0])
    v2 = Vertex(tup[1])
    g.insert_edge(v1,v2)
    
  colors = coloringBFS(g)
  polska.draw_map(g, [(node.id, color) for node, color in colors.items()])
  

if __name__ == "__main__":
  main()